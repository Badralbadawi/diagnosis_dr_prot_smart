from django.urls import path
from . import views
# from .views import DoctorRegisterView
from django.contrib.auth import views as authViews
from .views import DoctorSignupView,AdminDoctorApproveDetailView_d,profile, DoctorSignupSuccessView, AdminDoctorApproveView,profile_Docor,profile_assint, AdminDoctorApproveDetailView, DoctorDashboardView


urlpatterns = [
    # path('Sign', views.Admin , name='Admin'),
    path('userlogin/' ,views.userlogin, name="userlogin"),

    # path('export-pdf',views.export_pdf.as_view(),name='export-pdf'),
    # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('signup', DoctorSignupView.as_view(), name='doctor_signup'),
    path('success', DoctorSignupSuccessView.as_view(), name='doctor_signup_success'),
    path('admin_doctor_approve', AdminDoctorApproveView.as_view(), name='admin_doctor_approve'),
    path('admin_doctor_approve_detail/<int:pk>', AdminDoctorApproveDetailView.as_view(), name='admin_doctor_approve_detail'),
    path('dashboard/', DoctorDashboardView.as_view(), name='doctor_dashboard'),
    path('admin_doctor_approve_detail_doctors/<int:pk>', AdminDoctorApproveDetailView_d.as_view(), name='admin_doctor_approve_detail_doctors'),
    path('profile',views.profile_Docor,name='profile_Docor'),
    path('Profile_assint',views.profile_assint,name='Profile_assint'),
    path('profile',views.profile,name='profile'),
    path('',views.index,name='index' ),
    path('Doctor ', views.Doctor , name='Doctor'),
    path('Dr_assint ', views.dr_assint , name='Dr_assint'),
    path('patient/<int:patient_id>/', views.patient_record, name='patient_record'),
    path('website/details/<int:id>', views.details, name='details'),
    path('pdf',views.generate_pdf, name='generate_pdf'),
    path('Exam',views.exam,name='exam'),
    path('ta',views.requerd_pat,name='ta'),
    
    path('website/details/<int:id>',views.details, name='details'),
    path('userLogout/', views.userLogout,name='userLogout'),
      path('admin_doctor_approve/', AdminDoctorApproveView.as_view(), name='admin_doctor_approve'),
    path('admin_doctor_approve_detail/<int:pk>/', AdminDoctorApproveDetailView.as_view(), name='admin_doctor_approve_detail'),
    path('admin_doctor_approve_detail_d/<int:pk>/', AdminDoctorApproveDetailView_d.as_view(), name='admin_doctor_approve_detail_d'),
    
    
    path('reset_password/' ,authViews.PasswordResetView.as_view(template_name= "authentication/password_reset.html") , name="reset_password"),
    path('reset_password_sent/' ,authViews.PasswordResetDoneView.as_view(template_name= "authentication/password_reset_sent.html") , name="password_reset_done"),
    path('reset/<uidb64>/<token>/' ,authViews.PasswordResetConfirmView.as_view(template_name= "authentication/password_reset_form.html") , name="password_reset_confirm"),
    path('reset_password_complete/' ,authViews.PasswordResetCompleteView.as_view(template_name= "authentication/password_reset_done.html") , name="password_reset_complete"),


]

