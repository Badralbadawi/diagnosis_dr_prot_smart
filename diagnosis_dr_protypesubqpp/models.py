
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime

from django.db import models
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()
doctor_group = Group.objects.get(name='Doctor')
assistant_group = Group.objects.get(name='Dr_assint')

# دالة المستقبل لإضافة المستخدم إلى المجموعة المناسبة بعد تسجيله
@receiver(post_save, sender=User)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff and not instance.is_superuser:
            if instance.doctor:
                instance.groups.add(doctor_group)
            elif instance.assistant:
                instance.groups.add(assistant_group)
ch = [
    ('Man', 'Man'),
    ('Woman', 'Woman')
]
DIAGNOSIS_TYPE = [
    ('No_DR', 'No_DR'),
    ('Mild', 'Mild'),   
    ('Moderate', 'Moderate'),
    ('Severe', 'Severe'),
    ('Proliferate_DR', 'Proliferate_DR')
]

class Patient(models.Model):
    # اسم المريض
    name = models.CharField(max_length=32, default=None)

    # العمر
    age = models.CharField(max_length=3)

    # صورة المريض
    image = models.ImageField(upload_to='Photos/%y/%m/%d', default=None)

    # الجنس
    gender = models.CharField(max_length=8, choices=ch, default=None)

    # تاريخ الإنشاء
    date_created = models.DateTimeField(auto_now_add=True)
    

class Notes_doctor(models.Model):
    # المريض
    fn_patient = models.ForeignKey('DIAgnosis', on_delete=models.CASCADE)

    # الطبيب
    fn_doctor = models.ForeignKey('doctors', on_delete=models.CASCADE)

    # الملاحظات
    note = models.TextField()

    # تاريخ الإنشاء
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"مراجعة المريض {self.fn_patient} ورفع الملاحظات مع الدكتور {self.fn_doctor} في {self.created_at}"


class Dr_assint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    # اسم الطبيب المساعد
    name = models.CharField(max_length=40, default=None)

    # رقم الهاتف
    phone_number = models.IntegerField(default=None)
    #العنوان
    address = models.CharField(max_length=100)

    # مكان العمل
    workplace = models.CharField(max_length=25)

    # المؤهل العلمي
    qualification = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    # إضافة المزيد من الحقول الخاصة بالطبيب
    is_approved = models.BooleanField(default=False)
    gender = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def approve(self):
        self.is_approved = True
        self.save()
        subject = 'تم الموافقة على تسجيلك'
        message = render_to_string('email/approval.html')
        from_email = 'diagnosissmart@gmail.com'
        recipient_list = [self.email]
        send_mail(subject, message, from_email, recipient_list, html_message=message)


    def reject(self):
        self.delete()

    def __str__(self):
        return self.name


    # المالك

class doctors(models.Model):
    # المستخدم
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    # اسم الطبيب
    name = models.CharField(max_length=40, default=None)

    # رقم الهاتف
    phone_number = models.IntegerField(default=None)
    #العنوان
    address = models.CharField(max_length=100)

    # مكان العمل
    workplace = models.CharField(max_length=25)

    # المؤهل العلمي
    qualification = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    # إضافة المزيد من الحقول الخاصة بالطبيب
    is_approved = models.BooleanField(default=False)
    gender = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def approve(self):
        self.is_approved = True
        self.save()
        subject = 'تم الموافقة على تسجيلك'
        message = render_to_string('email/approval.html')
        from_email = 'diagnosissmart@gmail.com'
        recipient_list = [self.email]
        send_mail(subject, message, from_email, recipient_list, html_message=message)

    # def approve(self):
    #     self.is_approved = True
    #     self.save()

    def reject(self):
        self.delete()


    def __str__(self):
        return self.name


class DIAgnosis(models.Model):
    # المريض
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # الدقة
    accuracy = models.FloatField(default=0.0)

    # التشخيص
    predictions = models.CharField(max_length=20, choices=DIAGNOSIS_TYPE, default=None)

    # الرسم البياني
    plot = models.ImageField(upload_to='plots/')

    # تاريخ التشخيص
    diagnosis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.predictions} - {self.diagnosis_date}"

