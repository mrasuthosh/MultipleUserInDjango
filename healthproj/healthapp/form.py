from django.contrib.auth.forms import UserCreationForm
from . models import User , Doctor , Patient
from django.db import transaction
from django import forms

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    phone_number = forms.CharField(required = True)
    designation = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()

        patient = Patient.objects.create(user=user)
        patient.email_id = self.cleaned_data.get('email_id')
        patient.save()
        return User


class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    designation = forms.CharField(required = True)
    email = forms.CharField(required = True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()

        doctor = Doctor.objects.create(user=user)
        doctor.email_id = self.cleaned_data.get('email_id')
        doctor.designation = self.cleaned_data.get('designation')
        doctor.save()
        return User
