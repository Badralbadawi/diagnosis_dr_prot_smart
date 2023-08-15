from django.contrib import admin
from .models import Patient
from .models import doctors
from .models import Dr_assint
from .models import Notes_doctor,DIAgnosis
admin.site.register(Patient)
admin.site.register(Notes_doctor)
admin.site.register(DIAgnosis)
# Register your models here.
from django.contrib import admin
admin.site.site_header="Smart Diagnosis"
admin.site.site_title="Admin Smart Diagnosis"
@admin.register(doctors)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number','is_approved')
    actions = ['approve_doctors']

    def approve_doctors(self, request, queryset):
        for doctor in queryset:
            doctor.approve()
        self.message_user(request, 'تم الموافقة على تسجيل الأطباء بنجاح.')
    approve_doctors.short_description = 'موافقة الأطباء المحددين'

@admin.register(Dr_assint)
class Dr_assintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_approved')
    actions = ['approve_doctors']

    def approve_doctors(self, request, queryset):
        for doctor in queryset:
            doctor.approve()
        self.message_user(request, 'تم الموافقة على تسجيل المساعدين الطبيين بنجاح.')
    approve_doctors.short_description = 'موافقة المساعدين الطبيين المحددين'

# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def custom_admin_view(request):
    context = {'title': 'Custom Admin View'}
    return render(request, 'authentication/admin_doctor_approve.html.html', context=context)

class CustomAdminView(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('custom_admin_view/', self.admin_view(custom_admin_view)),
        ]
        return urls

custom_admin_site = CustomAdminView(name='custom_admin')

# custom_admin_view.html


