from . import views
from django.urls import path 

urlpatterns = [
    path("",views.home,name='home'),
    path("login",views.login.as_view(),name='login'),
    path("patient_register/",views.patient_register.as_view(),name='patient_register'),
    path("dr_register/",views.dr_register.as_view(),name='dr_register'),
    path("login_validation/",views.login_validation,name='login_validation'),
    path("logout/",views.logout,name='logout'),
]


