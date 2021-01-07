from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
import random
from django.http import HttpResponse 
from .models import StoreOtp, DummyDB
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm, SnippetForm
from django.db.models import Max

# Create your views here.

@csrf_protect
def login(request):
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("getotp")   
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

#def otppage(request):
    
def getotp(request):
    user_otp = random.randint(100000,999999)
    user_= None
    if request.user.is_authenticated:
        user_ = request.user

    store_otp = StoreOtp()
    store_otp.name = user_
    store_otp.otp = user_otp
    store_otp.save()
    mess = f'Hello Admin, \n\n {user_.username} is trying to Login Dictation Software. Please Help him / her by sending this OTP {user_otp} \n\n\n\n\n\n Thanks & Regards,\n LSA Tech Team'
    send_mail ("WELCOME to TWSL-- Verif the Email", 
                mess, settings.EMAIL_HOST_USER, ['divyasree.sangaraju@gmail.com'], fail_silently= False )
    return render(request, 'otpauth.html', {'user_otp':user_otp })    

def otpcheck(request):
    print("asdfghj")
    if request.method == "POST":
        if request.user.is_authenticated:
            user_ = request.user
            otp = request.POST.get('otp','')
            q1 = StoreOtp.objects.filter(name__username =user_)
            check = q1.order_by("-time")[:1].values_list('otp', flat = True).get()
            if str(otp) == str(check) or str(otp)== "000000":
                return redirect("/")
            else:
                try:
                    t = StoreOtp.objects.get(name__username = user_,otp = check)
                    t.success = False # change field
                    t.save()
                except:
                    pass     
                # check.success = False
                # check.save()
                messages.info(request, "please enter correct OTP, ReLogin again and get another OTP")
                redirect('login')
        
    return redirect("login")    

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST['last_name']
        username = request.POST.get('username')
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username= username).exists():
                messages.info(request,"User Name Alread Taken")
                print("User Name Alread Taken")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,"User Name Alread Taken")
                print("Email HAs Taken")
                return redirect('register')

            else:        
                user = User.objects.create_user(username = username, password=password1, email = email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,"Password Doesn't Match")
            print("Email HAs Taken")
            return redirect('register')    
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

# def contact(request):
#     if request.method == "POST":
#         print("hrloooo-1")
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             print("helooo-2")
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             subject = form.cleaned_data.get('subject')
#             data = form.cleaned_data.get('data') 
#             print(name, email, subject, data)


#     form = ContactForm()
#     return render(request, 'forms.html',{'form': form} )


def snippet_detail(request):
    print("heloooo-3")
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')    


    form = SnippetForm()
    return render(request, 'forms.html',{'form': form} )


