from django import forms
from .models import Notes_doctor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dr_assint,doctors

class NotesDoctorForm(forms.ModelForm):
    class Meta:
        model = Notes_doctor
        fields = ('note', )
        



class DoctorProfileForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.IntegerField()
    workplace = forms.CharField(max_length=25)
    address = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('Man', 'Male'), ('Woman', 'Famle ')], required=True)

    qualification = forms.CharField(max_length=20)
    user_type = forms.ChoiceField(choices=[('doctor', 'Doctor'), ('assistant', 'Assistant')], required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'user_type')

    def save(self, commit=True):

        user = super().save(commit=True)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        if self.cleaned_data["user_type"] == 'doctor':
            doctor = doctors.objects.create(user=user, name=self.cleaned_data["first_name"]+" "+self.cleaned_data["last_name"], phone_number=self.cleaned_data['phone_number'], workplace=self.cleaned_data["workplace"], address=self.cleaned_data["address"], gender=self.cleaned_data["gender"], qualification=self.cleaned_data["qualification"],email=self.cleaned_data["email"])
            return doctor
        else:
            assistant = Dr_assint.objects.create(user=user, name=self.cleaned_data["first_name"]+" "+self.cleaned_data["last_name"], phone_number=self.cleaned_data['phone_number'], workplace=self.cleaned_data["workplace"], address=self.cleaned_data["address"], gender=self.cleaned_data["gender"], qualification=self.cleaned_data["qualification"],email=self.cleaned_data["email"])
            return assistant
    

