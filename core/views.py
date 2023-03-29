from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient, Professional
from .forms import PatientForm, ProForm #,SignUpForm
from datetime import datetime, timedelta
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin/admin_login.html')

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username'] #admin
#         password = request.POST['password'] #123
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('admin_dashboard') 
#         else:
#             # Authentication failed
#             error_message = "Invalid Login Credentials. Please Try Again."
#             return render(request, 'admin/admin_login.html', {'error_message': error_message})
#     else:
#         return render(request, 'admin/admin_login.html')


# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         # Retrieve the number of failed attempts from the session
#         login_attempts = request.session.get('login_attempts', 0)
#         lock_timestamp = request.session.get('lock_timestamp', None)

#         # Check if the lock duration has passed
#         if lock_timestamp and datetime.now() - lock_timestamp >= timedelta(minutes=5):
#             login_attempts = 0
#             lock_timestamp = None

#         if login_attempts < 3:
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Clear the failed attempts counter upon successful login
#                 request.session['login_attempts'] = 0
#                 request.session['lock_timestamp'] = None
#                 return redirect('admin_dashboard')
#             else:
#                 # Authentication failed
#                 login_attempts += 1
#                 request.session['login_attempts'] = login_attempts
#                 error_message = "Invalid login credentials. Please try again."
#         else:
#             if not lock_timestamp:
#                 # Save the lock timestamp
#                 request.session['lock_timestamp'] = datetime.now()
#             error_message = "Your account has been locked due to too many failed login attempts. Please try again after 5 minutes."

#         return render(request, 'admin/admin_login.html', {'error_message': error_message})

#     else:
#         return render(request, 'admin/admin_login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Retrieve the number of failed attempts from the session
        login_attempts = request.session.get('login_attempts', 0)
        lock_timestamp = request.session.get('lock_timestamp', None)

        if lock_timestamp:
            lock_timestamp = datetime.strptime(lock_timestamp, "%Y-%m-%d %H:%M:%S.%f")

            # Check if the lock duration has passed
            if datetime.now() - lock_timestamp >= timedelta(minutes=5):
                login_attempts = 0
                lock_timestamp = None
                request.session['login_attempts'] = login_attempts
                request.session['lock_timestamp'] = None

        if login_attempts < 3:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Clear the failed attempts counter upon successful login
                request.session['login_attempts'] = 0
                request.session['lock_timestamp'] = None
                return redirect('admin_dashboard')
            
        # Authentication failed
        login_attempts += 1
        request.session['login_attempts'] = login_attempts
        error_message = "Invalid login credentials. Please try again."

        if login_attempts == 3:
            lock_timestamp = datetime.now()
            request.session['lock_timestamp'] = lock_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            error_message = "Your Account Has Been Locked Due To Too Many Failed Login Attempts. Please Try Again After 5 Minutes."

        return render(request, 'admin/admin_login.html', {'error_message': error_message})
    else:
        return render(request, 'admin/admin_login.html')

    
#Logout
# @login_required(login_url = 'admin_dashboard')
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url = 'admin_login')
@never_cache
def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')

@login_required(login_url = 'admin_login')
@never_cache
def patient_data(request):
    patients = Patient.objects.all()
    return render(request,'admin/patient_data.html',{'patients': patients})

@login_required(login_url = 'admin_login')
@never_cache
def pro_data(request):
    professionals = Professional.objects.all()
    return render(request,'admin/pro_data.html')


# def patient_login(request):
#     return render(request,'patient/patient_login.html')

def patient_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        form = AuthenticationForm(data = request.POST)

        if user is not None:
            login(request, user)
            return redirect('patient_dashboard')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'patient/patient_login.html')


# def patient_register(request):
#     if request.method == "POST":

#         user_form = SignUpForm(request.POST)
#         profile_form = Patient(request.POST, request.FILES)
        
#         if user_form.is_valid() and profile_form.is_valid():
            
#             user = user_form.save()
#             #user.set_password(user.password)
#             #user.is_active = False #New
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user

#             if request.FILES:
#                 profile.profile_pic = request.FILES['profile_pic']

#             profile.save()


#             username1 = user_form.cleaned_data['username']
#             password1 = user_form.cleaned_data['password1']
#             user = authenticate(request, username=username1, password=password1)
#             if user is not None:
#                 login(request, user)
#                 profile = Patient.objects.get(user=request.user)
                
#             messages.success(request,("You have been Registered ..."))
#             return redirect('student:home')


#     else:
#         user_form = SignUpForm()
#         profile_form = PatientForm()

#     return render(request,'auth/patient/patient_register.html',{'user_form':user_form,'profile_form':profile_form,'title':'Register'})

 

def patient_register(request):
    if request.method == "POST":

        form = PatientForm(request.POST)

        full_name = request.POST["full_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        phone = request.POST["phone"]
        dob = request.POST["dob"]
        gender = request.POST["gender"]
        city = request.POST["city"]
        state = request.POST["state"]

        # First, create and save the User object with the provided password
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        # Then, create and save the Patient object associated with the User object
        patient = Patient(user=user, full_name=full_name, email=email, phone=phone, dob=dob, gender=gender, city=city, state=state)
        patient.save()

        return redirect('patient_dashboard')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_register.html', {'form': form})

# def patient_login(request):
#     if  request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email = email, password = password)
#         form = AuthenticationForm(data = request.POST)
        
#         if user is not None: 
#             login(request, user)
#            # messages.success(request, 'Successfully Logged In ')
#             return redirect('patient_dashboard')
        
#         # else:
#         #     return redirect (''patient/patient_login.html'')
        
#     else:
#         pass
#         form = AuthenticationForm()
#     return render(request, 'patient_login.html')

# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username'] #admin
#         password = request.POST['password'] #123
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('admin_dashboard') 
#         else:
#             # Authentication failed
#             error_message = "Invalid login credentials. Please try again."
#             return render(request, 'admin/admin_login.html', {'error_message': error_message})
#     else:
#         return render(request, 'admin/admin_login.html')

def patient_logout(request):
    logout(request)
    return redirect('patient_login')


# def patient_register(request):
#     return render(request,'patient/patient_register.html')

@login_required(login_url = 'patient_login')
@never_cache
def patient_dashboard(request):
    return render(request,'patient/patient_dashboard.html')

# Registration code v1
# def patient_register(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)

#         form.full_name = request.POST["full_name"]
#         form.email = request.POST["email"]
#         form.phone = request.POST["phone"]
#         form.dob = request.POST["dob"]
#         form.gender = request.POST["gender"]
#         form.city = request.POST["city"]
#         form.state = request.POST["state"]
       
#         if form.is_valid():
#             form.save()
#             print("Patient")
#             return redirect('patient_dashboard')

#     else:
#         form = PatientForm()
#     return render(request, 'patient/patient_register.html',{'form': form})


# Registration code v2
# def patient_register(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)

#         if form.is_valid():
#             patient = form.save(commit=False)
#             patient.full_name = form.cleaned_data["full_name"]
#             patient.email = form.cleaned_data["email"]
#             patient.phone = form.cleaned_data["phone"]
#             patient.dob = form.cleaned_data["dob"]
#             patient.gender = form.cleaned_data["gender"]
#             patient.city = form.cleaned_data["city"]
#             patient.state = form.cleaned_data["state"]
#             patient.save()

#             print("Patient")
#             return redirect('patient_dashboard')

#     else:
#         form = PatientForm()
#     return render(request, 'patient/patient_register.html', {'form': form})


# Patient Registration V3
# def patient_register(request):
#     if request.method == "POST":
#         form = PatientForm(request.POST)

#         if form.is_valid():
#             # Create a new User instance with the provided email and a default password
#             user = User.objects.create_user(
#                 username=form.cleaned_data['email'],
#                 email=form.cleaned_data['email'],
#                 password='default_password',
#             )

#             # Associate the new User instance with the Patient instance
#             patient = form.save(commit=False)
#             patient.user = user
#             patient.save()

#             return redirect('patient_dashboard')

#     else:
#         form = PatientForm()
#     return render(request, 'patient/patient_register.html', {'form': form})


def pro_login(request):
    if request.method == 'POST':
        email = request.POST['email'] 
        password = request.POST['password'] 
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('pro_dashboard') 
        else:
            # Authentication failed
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'professional/pro_login.html', {'error_message': error_message})
    else:
        return render(request, 'professional/pro_login.html')
    

#Professional Registration V4
def pro_register(request):
    if request.method == "POST":

        # First, create and save the User object with the provided password
        email = request.POST["email"]
        password = request.POST["password"]
        
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
        except:
            messages.warning(request, 'user with this email already exists!')
            form = ProForm()
            return render(request, 'professional/pro_register.html', {'form': form})


        try:

            professional = Professional()
            professional.user = user
            professional.pro_type = request.POST["pro_type"]
            professional.first_name = request.POST["first_name"]
            professional.last_name = request.POST["last_name"]
            professional.dob = request.POST["dob"]
            professional.gender = request.POST["gender"]
            professional.email = request.POST["email"]
            professional.phone = request.POST["phone"]
            professional.city = request.POST["city"]
            professional.state = request.POST["state"]
            professional.zip = request.POST["zip"]
            professional.edu_type = request.POST["edu_type"]
            professional.license = request.POST["license"]
            professional.nid_passport = request.POST["nid_passport"]
            professional.save()

            return redirect('pro_login')

        except:
            user.delete()
            messages.warning(request, "error occurred while saving 'Professional' profile ")

    else:
        form = ProForm()

    return render(request, 'professional/pro_register.html', {'form': form})


# Professional Register
# def pro_register(request):
#     return render(request,'professional/pro_register.html')

#Professional Registration V1 not working
# def pro_register(request):
#     if request.method == "POST":
#         form = ProForm(request.POST)

#         form.pro_type = request.POST["title"]
#         form.full_name = request.POST["first_name"]
#         form.last_name = request.POST["last_name"]
#         form.dob = request.POST["dob"]
#         form.gender = request.POST["gender"]
#         form.email = request.POST["email"]
#         form.phone = request.POST["phone"]
#         form.city = request.POST["city"]
#         form.state = request.POST["state"]
#         form.zip = request.POST["zip"]
#         form.edu_type = request.POST["qualification"]
#         form.license = request.POST["license"]
#         form.nid_passport = request.POST["nid_passport"]
       
#         if form.is_valid():
#             form.save()
#             print("Professional")
#             return redirect('pro_dashboard')

#     else:
#         form = ProForm()
#     return render(request, 'professional/pro_register.html', {'form': form})

#Professional Registration V2
# def pro_register(request):
#     if request.method == "POST":
#         form = ProForm(request.POST)

#         if form.is_valid():
#             pro = form.save(commit=False)
            
#             pro.pro_type = request.POST["title"]
#             pro.full_name = request.POST["first_name"]
#             pro.last_name = request.POST["last_name"]
#             pro.dob = request.POST["dob"]
#             pro.gender = request.POST["gender"]
#             pro.email = request.POST["email"]
#             pro.phone = request.POST["phone"]
#             pro.city = request.POST["city"]
#             pro.state = request.POST["state"]
#             pro.zip = request.POST["zip"]
#             pro.edu_type = request.POST["qualification"]
#             pro.license = request.POST["license"]
#             pro.nid_passport = request.POST["nid_passport"]

#             pro.save()
#             print("Professional")
#             return redirect('pro_dashboard')

#     else:
#         form = ProForm()
#     return render(request, 'professional/pro_register.html', {'form': form})

#Professional Registration V3
# def pro_register(request):
#     if request.method == "POST":
#         form = ProForm(request.POST)

#         if form.is_valid():
#             form.save()
#             print("Professional")
#             return redirect('pro_dashboard')

#     else:
#         form = ProForm()
#     return render(request, 'professional/pro_register.html', {'form': form})





# @login_required(login_url = 'pro_login')
# def pro_dashboard(request):
#     return render(request,'professional/pro_dashboard.html')


@login_required(login_url = 'pro_login')
@never_cache
def pro_dashboard(request):
    professionals = Professional.objects.all()
    print("Professionals:", professionals)
    return render(request, 'professional/pro_dashboard.html', {'professionals': professionals})



