'''
# from audioop import reverse
# import random
# from django.shortcuts import render,HttpResponse,redirect 
# from django.template import loader
# from django.views import View
# from .models import Patient,doctors,Dr_assint,DIAgnosis,Notes_doctor
# import numpy as np

# from django.contrib import messages
# from io import BytesIO

# from reportlab.lib.pagesizes import letter

# from django.contrib.auth import authenticate ,login  , logout 
# from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# import tensorflow as tf
# import matplotlib.pyplot as plt
# import os
# from  tensorflow import keras
# from django.http import HttpResponse
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas
# from reportlab.lib.utils import ImageReader
# from .forms import NotesDoctorForm
# from reportlab.pdfgen import canvas
# from .decorators import allowedUsers

# from io import BytesIO
# from django.conf import settings
# from django.shortcuts import render, redirect
# from .forms import NotesDoctorForm,DoctorProfileForm
# import qrcode
# from django.contrib import messages
# from .decorators import forAdmins,allowedUsers
# from django.urls import reverse
# from django.views.generic import DetailView
# from django.views import View
# from .forms import DoctorProfileForm

# from django.views import View
# from .models import doctors,Dr_assint

# from django.views.generic import DetailView






# class DoctorSignupView(View):
#     template_name = 'authentication/signup.html'

#     def get(self, request):
#         form = DoctorProfileForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = DoctorProfileForm(request.POST)
#         if form.is_valid():
#             doctor = form.save(commit=True)
#             doctor.is_approved = False
#             doctor.save()
#             # إرسال إشعار إلى المشرف
#             return redirect('doctor_signup_success')
#         else:
#             return render(request, self.template_name, {'form': form})
# class DoctorSignupSuccessView(View):
#     template_name = 'authentication/doctor_signup_success.html'

#     def get(self, request):
#         return render(request, self.template_name)
# class AdminDoctorApproveView(View):
#     # model=Dr_assint

#     template_name = 'authentication/admin_doctor_approve.html'

#     def get(self, request):
#             unapproved_doctors =doctors.objects.filter(is_approved=False)
           
#             unapproved_assinet= Dr_assint.objects.filter(is_approved=False)

#             return render(request, self.template_name, {'doctors': unapproved_doctors,'assinet':unapproved_assinet})


# class AdminDoctorApproveDetailView(DetailView):
#     model=Dr_assint
#     template_name = 'authentication/admin_doctor_approve_detail.html'
#     # template_name = 'authentication/admin_doctor_approve.html'
#     def post(self, request,pk):
#         # ass=Dr_assint.objects.get(id=pk)

#         doctor = self.get_object()

#         if 'approve' in request.POST:
#             doctor.approve()

#         elif 'reject' in request.POST:
#             doctor.reject()
#         return redirect(reverse('admin_doctor_approve'))

# class AdminDoctorApproveDetailView_d(DetailView):
#     # model=doctors
#     model=doctors
#     template_name = 'authentication/admin_doctor_approve_detail_doctors.html'
#     # template_name = 'authentication/admin_doctor_approve.html'

#     def post(self, request, pk):
#         doctor = self.get_object()
#         if 'approve' in request.POST:
#             doctor.approve()
#         elif 'reject' in request.POST:
#             doctor.reject()
#         return redirect(reverse('admin_doctor_approve'))

# class DoctorDashboardView(View):
#     template_name = 'authentication/doctor_dashboard.html'

#     def get(self, request):
#         doctor = doctors.objects.get(user=request.user)
#         return render(request, self.template_name, {'doctor': doctor})
'''
# استيراد المكتبات اللازمة
from audioop import reverse
import random
from django.shortcuts import render,HttpResponse,redirect 
from django.template import loader
from django.views import View
from .models import Patient,doctors,Dr_assint,DIAgnosis,Notes_doctor
import numpy as np
from django.contrib import messages
from io import BytesIO
from reportlab.lib.pagesizes import letter
from django.contrib.auth import authenticate ,login  , logout 
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from  tensorflow import keras
from django.http import HttpResponse
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .forms import NotesDoctorForm
import qrcode
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import NotesDoctorForm,DoctorProfileForm
from .decorators import allowedUsers, forAdmins
from django.urls import reverse
from django.views.generic import DetailView

# إنشاء عرض الصفحة الخاصة بتسجيل الأطباء
class DoctorSignupView(View):
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = DoctorProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=True)
            doctor.is_approved = False
            doctor.save()
            # إرسال إشعار إلى المشرف
            return redirect('doctor_signup_success')
        else:
            return render(request, self.template_name, {'form': form})

# إنشاء عرض الصفحة الخاصة بنجاح تسجيل الأطباء
class DoctorSignupSuccessView(View):
    template_name = 'authentication/doctor_signup_success.html'

    def get(self, request):
        return render(request, self.template_name)

# إنشاء عرض الصفحة الخاصة بموافقة المشرف على حسابات الأطباء
class AdminDoctorApproveView(View):
    template_name = 'authentication/admin_doctor_approve.html'

    def get(self, request):
        # عرض جميع الأطباء الذين لم يتم موافقة على حساباتهم
        unapproved_doctors = doctors.objects.filter(is_approved=False)
        unapproved_assinet = Dr_assint.objects.filter(is_approved=False)
        return render(request, self.template_name, {'doctors': unapproved_doctors,'assinet':unapproved_assinet})

# إنشاء عرض الصفحة الخاصة بموافقة المشرف على حسابات الأطباء بالتفصيل
class AdminDoctorApproveDetailView(DetailView):
    model = Dr_assint
    template_name = 'authentication/admin_doctor_approve_detail.html'

    def post(self, request, pk):
        doctor = self.get_object()
        if 'approve' in request.POST:
            doctor.approve()
        elif 'reject' in request.POST:
            doctor.reject()
        return redirect(reverse('admin_doctor_approve'))

# إنشاء عرض الصفحة الخاصة بموافقة المشرف على حسابات الأطباء بالتفصيل
class AdminDoctorApproveDetailView_d(DetailView):
    model = doctors
    template_name = 'authentication/admin_doctor_approve_detail_doctors.html'

    def post(self, request, pk):
        doctor = self.get_object()
        if 'approve' in request.POST:
            doctor.approve()
        elif 'reject' in request.POST:
            doctor.reject()
        return redirect(reverse('admin_doctor_approve'))

# إنشاء عرض لوحة تحكم الأطباء
class DoctorDashboardView(View):
    template_name = 'authentication/doctor_dashboard.html'

    def get(self, request):
        doctor = doctors.objects.get(user=request.user)
        return render(request, self.template_name, {'doctor': doctor})
'''
# def add_medical_note(request, patient, form):
#     if form.is_valid():
#         note = form.save(commit=False)
#         note.fn_patient = patient
#         note.fn_doctor = request.user.doctor
#         note.save()
#         return redirect('patient_record', patient_id=patient.id)
#     else:
#         print('error')

# def patient_record(request, patient_id):
#     patient = DIAgnosis.objects.get(patient=patient_id)
#     medical_notes = Notes_doctor.objects.filter(fn_patient=patient)
#     form = NotesDoctorForm()

#     if request.method == 'POST':
#         form = NotesDoctorForm(request.POST)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.fn_patient = patient
#             note.fn_doctor = request.user.doctors
#             note.save()
#             form = NotesDoctorForm()
#             member = None
#             note = None
#             medical_notes = None
#         else:
#             print('error')

#     context = {
#         'patient': patient,
#         'medical_notes': medical_notes,
#         'form': form,
#     }
#     return render(request, 'diagnosis_dr/patient_record.html', context)

# @login_required(login_url='userlogin')
# @forAdmins
# def Doctor(request):
#     member = None
#     note = None
#     form = NotesDoctorForm()
#     medical_notes = None
    
#     if request.method == 'POST':
#         search = request.POST.get("search")
#         form = NotesDoctorForm(request.POST)
        
#         if search.isdigit():
#             member = DIAgnosis.objects.get(patient=int(search))
            
#             if form.is_valid():
#                 note = form.save(commit=False)
#                 note.fn_patient = member
#                 note.fn_doctor = request.user.doctors
#                 note.save()
#                 messages.success(request, "Note added successfully!")
#                 return redirect("Doctor")

#     context = {
#         "Members": member,
#         "data": note,
#         "medical_notes": medical_notes,
#         "form": form,
#     }  
#     return render(request, "diagnosis_dr/Doctor.html", context)

# # Define the custom layer or function
# class FixedDropout(keras.layers.Dropout):
#     def call(self, inputs, training=None):
#         if training is None:
#             training = keras.backend.learning_phase()
#         return super().call(inputs, training)

# # Register the custom layer or function
# keras.utils.get_custom_objects().update({'FixedDropout': FixedDropout})
# model = keras.models.load_model('models__DR (4).h5')


# def userlogin(request):
#         if request.method == 'POST': 
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request , username=username, password=password)
#             if user is not None:
#                 login(request, user) 
#                 request.session['doctor_username'] = username
#                 return redirect('profile_Docor')
#             else:
#                 messages.info(request, 'Credentials error')

#         context = {}

#         return render(request , 'diagnosis_dr/Admin.html' ,context )
 '''
def userLogout(request):  
    logout(request)
    return redirect('userlogin')
  
 # استيراد المكتبات اللازمة

# إضافة ملاحظة طبية جديدة للمريض
def add_medical_note(request, patient, form):
    if form.is_valid():
        note = form.save(commit=False)
        note.fn_patient = patient
        note.fn_doctor = request.user.doctor
        note.save()
        return redirect('patient_record', patient_id=patient.id)
    else:
        print('error')

# عرض سجل المريض
def patient_record(request, patient_id):
    patient = DIAgnosis.objects.get(patient=patient_id)
    medical_notes = Notes_doctor.objects.filter(fn_patient=patient)
    form = NotesDoctorForm()

    if request.method == 'POST':
        form = NotesDoctorForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.fn_patient = patient
            note.fn_doctor = request.user.doctors
            note.save()
            form = NotesDoctorForm()
            member = None
            note = None
            medical_notes = None
        else:
            print('error')

    context = {
        'patient': patient,
        'medical_notes': medical_notes,
        'form': form,
    }
    return render(request, 'diagnosis_dr/patient_record.html', context)

# صفحة لوحة تحكم الأطباء
@login_required(login_url='userlogin')
@forAdmins
def Doctor(request):
    member = None
    note = None
    form = NotesDoctorForm()
    medical_notes = None
    
    if request.method == 'POST':
        search = request.POST.get("search")
        form = NotesDoctorForm(request.POST)
        
        if search.isdigit():
            member = DIAgnosis.objects.get(patient=int(search))
            
            if form.is_valid():
                note = form.save(commit=False)
                note.fn_patient = member
                note.fn_doctor = request.user.doctors
                note.save()
                messages.success(request, "Note added successfully!")
                return redirect("Doctor")

    context = {
        "Members": member,
        "data": note,
        "medical_notes": medical_notes,
        "form": form,
    }  
    return render(request, "diagnosis_dr/Doctor.html", context)

# إنشاء طبقة أو وظيفة مخصصة
class FixedDropout(keras.layers.Dropout):
    def call(self, inputs, training=None):
        if training is None:
            training = keras.backend.learning_phase()
        return super().call(inputs, training)

# تسجيل الطبقة أو الوظيفة المخصصة
keras.utils.get_custom_objects().update({'FixedDropout': FixedDropout})
model = keras.models.load_model('models__DR (4).h5')

# صفحة تسجيل الدخول للمستخدمين
def userlogin(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user) 
            request.session['doctor_username'] = username
            return redirect('profile_Docor')
        else:
            messages.info(request, 'Credentials error')

    context = {}

    return render(request , 'diagnosis_dr/Admin.html' ,context )

 


media='media'
media1='media/plots'
categories = [ 'No_DR','Mild', 'Moderate', 'Severe', 'Proliferate_DR']

def predict_DR(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path)
    image = image.resize((224,224))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0
    scaled_img = np.expand_dims(image_array, axis=0)

    # Use model to predict the sample image
    pred = model.predict(scaled_img)

    # Get the output
    output = categories[np.argmax(pred)]
    accuracy = pred[0][np.argmax(pred)]*100

    # Create a bar chart of the predictions
    plt.figure(figsize=(8, 6))
    plt.bar(categories, pred[0])
    plt.title("Diagnosis Prediction")
    plt.xlabel("Diagnosis")
    plt.ylabel("Probability")

    # Generate a unique filename for the plot
    random_num = random.randint(10000, 99999)
    filename = f"plot_{random_num}.png"

    # Convert the plot to an image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Save the plot to the storage location
    fs = FileSystemStorage(location='media/plots')
    fs.save(filename, buffer)

    # Get the URL for the saved plot
    plot_url = fs.url(filename)

    # Get the full path of the saved plot
    plot_path = os.path.join(fs.location, filename)

    return {'diagnosis': output, 'accuracy': accuracy, 'plot': plot_path}
@login_required

def profile(request):
    if request.user.groups.filter(name='Doctor').exists():
        # Redirect to doctor profile page
        return redirect('profile_assint')
    elif request.user.groups.filter(name='Dr_assint').exists():
        # Redirect to assistant profile page
        return redirect('profile_Docor')
@login_required(login_url='userlogin')
@forAdmins
def profile_Docor(request):
    

    usera=request.user.doctors
    print(usera)
    mydata_a = doctors.objects.get(user=usera)
    context = {
    'mymembers': mydata_a,
  }
    return render(request,'diagnosis_dr/profile_doctor.html',context)

@login_required(login_url='userlogin')
@allowedUsers(allowedGroups=['Dr_assint'])
def profile_assint(request):
        user_a=request.user
        mydata_a = Dr_assint.objects.get(user=user_a)

        return render(request,'diagnosis_dr/profile_assinet.html',{'assint': mydata_a})


        





def dr_assint(request):
    if request.method == "POST" and 'image' in request.FILES:
        Name = request.POST.get('name')
        Age = request.POST.get('age')
        Image = request.FILES.get('image')
        Gender = request.POST.get('gender')

        fss = FileSystemStorage()
        file = fss.save(Image.name, Image)

        # Get the diagnosis and the URL of the plot image
        prediction = predict_DR(os.path.join(settings.MEDIA_ROOT, file))

        # Save the patient information, the diagnosis, and the URL of the plot image in the database
        new_patient = Patient.objects.create(name=Name, age=Age, image=file, gender=Gender)
        new_diagnosis = DIAgnosis(patient=new_patient, accuracy=prediction['accuracy'], plot=prediction['plot'], predictions=prediction['diagnosis'])
        new_diagnosis.save()

        # Set session variable to indicate that a report is ready
        request.session['rp'] = 0

        messages.success(request, "Note added successfully!")

        # Generate and return the report if the session variable is set
        if 'rp' in request.session and request.session['rp'] == 0:
            # Extract patient information from tablepatsub using the primary key (id)
            pat = DIAgnosis.objects.get(patient=new_patient)

            # Create a QR code using qrcode
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(f"{pat.patient.id},{pat.patient.name},{pat.patient.age},{pat.patient.gender}")
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code as a file
            qr_file_name = f"{pat.patient.id}.png"
            img_path = os.path.join(settings.MEDIA_ROOT, "qr_codes", qr_file_name)
            img.save(img_path)

            # Update the patient record to include the QR code file name
            pat.qr_code = f"qr_codes/{qr_file_name}"
            pat.save()

            # Create a PDF file as a medical report using reportlab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pat.patient.name}_medical_report.pdf"'

            pdf_canvas = canvas.Canvas(response, pagesize=letter)
            pdf_canvas.setFont("Helvetica-Bold", 14)
            pdf_canvas.drawString(1 * inch, 10 * inch, "Medical Report")
            pdf_canvas.setFont("Helvetica", 12)
            pdf_canvas.drawString(1 * inch, 9.5 * inch, f"ID: {pat.patient.id}")
            pdf_canvas.drawString(1 * inch, 9 * inch, f"Name: {pat.patient.name}")
            pdf_canvas.drawString(1 * inch, 8.5 * inch, f"Age: {pat.patient.age}")
            pdf_canvas.drawString(1 * inch, 8 * inch, f"Gender: {pat.patient.gender}")

            # Load the QR code image and add it to the document
            qr_code_path = os.path.join(settings.MEDIA_ROOT, pat.qr_code)
            qr_code_img = ImageReader(qr_code_path)
            pdf_canvas.drawImage(qr_code_img, 1*inch, 7*inch, width=2*inch, height=2*inch)

            pdf_canvas.showPage()
            pdf_canvas.save()

            del request.session['rp']  # Remove the session variable
            
            # Define the context dictionary to render the template
           

            
            # Render the template with the context dictionary
            with open(f"{pat.patient.name}_medical_report.pdf", 'wb') as f:
                f.write(response.content)

            # Return an empty HTTP response to indicate success
            return response
        return redirect('dr_assint')
        # Return an error HTTP response if the session variable is not set

    # Return an empty HTTP response if the request method is not POST or 'image' is not in request.FILES
    return render(request, 'website/Dr_assint.html')
    # Return an empty response if the request method is not POST or 'image' is not in request.FILES
  #


def details(request, id):
  mymember = Patient.objects.get(id=id)
  notess=Notes_doctor.objects.filter(id=id)
  template = loader.get_template('diagnosis_dr/exam.html')
  context = {
    'mymember': mymember,
    'notes_doctor':notess,
  }
  return HttpResponse(template.render(context, request))
def requerd_pat(request):
    user=request.user.doctors
    # doctor = Doctor.objects.get(field=user)
    mydata = Notes_doctor.objects.filter(fn_doctor=user)

    template = loader.get_template('diagnosis_dr/ta.html')
    context = {
    'mymembers': mydata,
  }
    return HttpResponse(template.render(context, request))

def index(request):

    return render(request,'website/index.html')

def generate_pdf(pat):
    # Retrieve data from the database
    data = Patient.objects.filter(id=pat)
    if not data.exists():
        # messages.info(str(pat),"")
        return HttpResponse('Patient does not exist')


    d=DIAgnosis.objects.get(patient=pat)
    medical_notes = Notes_doctor.objects.filter(fn_patient=d)
    
    # Generate a file-
    # Create a new PDF object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{d.patient.name}_medical_report.pdf"'
    pdf = canvas.Canvas(response, pagesize=letter)

    # Add content to the PDF
    pdf.setTitle("Medical Report")
    pdf.setFillColorRGB(0.2, 0.2, 0.2)
    pdf.setFontSize(24)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(inch * 4.25, inch * 10, "Medical Report")
    pdf.line(inch, inch * 9.5, inch * 7, inch * 9.5)

    pdf.setFontSize(14)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(inch, inch * 9, f"Name: {d.patient.name}")
    pdf.drawString(inch, inch * 8.75, f"Age: {d.patient.age}")
    pdf.drawString(inch, inch * 8.5, f"Gender: {d.patient.gender}")
    pdf.drawString(inch, inch * 8.25, f"Image: {d.patient.image.url}")
    pdf.drawString(inch, inch * 8, f"Predictions: {d.predictions}")
    pdf.drawString(inch,inch*7.75, f"percent {d.accuracy}")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(inch, inch * 7, "Medical History")
    pdf.line(inch, inch * 6.9, inch * 7, inch * 6.9)

    pdf.setFont("Helvetica", 12)
    y = inch * 6.5
    for note in medical_notes:
        pdf.drawString(1.5 * inch, y, f"Date: {note.created_at}")
        pdf.drawString(1.5 * inch, y-20, f"Notes: {note.note}")
        pdf.drawString(1.5 * inch, y-40, f"Doctor Name: {note.fn_doctor.name}")
        pdf.drawString(1.5 * inch, y-80, f"Phone Number: {note.fn_doctor.phone_number}")
        pdf.drawString(1.5 * inch, y-100, f"Workplace: {note.fn_doctor.workplace}")

        y -= 60


    pdf.drawImage(d.patient.image.path,  100-inch, y-5*inch, width=3*inch, height=3*inch)
    pdf.drawImage(d.plot.path, 3.5 * inch, y-5*inch, width=5*inch, height=4*inch)
    pdf.showPage()

    # Close the PDF object cleanly, and return the response
    pdf.save()
    return response
def exam(request):
    if request.method == 'POST':
        # Retrieve the patient ID from the form
        pat_id = request.POST.get('pat_id')
        data = Patient.objects.filter(id=pat_id)
        if not data.exists():
            messages.info(request,"Patient does not exist")

            return render(request, 'diagnosis_dr/exam.html')
        # Generate the PDF file for the patient ID
        else:
            response = generate_pdf(pat_id)
            request=None

            return response
        # Set the response headers to trigger a download of the PDF file
    return render(request, 'diagnosis_dr/exam.html')


