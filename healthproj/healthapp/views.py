from django.shortcuts import render , redirect
from django.contrib import messages
from healthapp.form import PatientSignUpForm, DoctorSignUpForm
from . models import User , Patient , Doctor
from django.views.generic import CreateView , TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
# Create your views here.

def home(request):
    return render(request,'register.html')


class dr_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'dr_register.html'
    success_url = reverse_lazy('login')



    def validation(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('login')


class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'c_register.html'
    success_url = reverse_lazy('login')

    def validation(self,form,):
        user = form.save()
        login(self.request,user)
        return redirect('p_page')

class login(TemplateView):
    template_name = 'login.html'
 
def login_validation(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                auth_login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
                
    return render(request,'login.html',context={'form':AuthenticationForm()})


def logout(request):
    logout(request)
    return redirect('home')
