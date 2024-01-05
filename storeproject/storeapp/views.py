from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Store



# Create your views here.
def base(request):
    return render(request, template_name='base.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('storeapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, 'registered successfully')
                return redirect('storeapp:login')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('storeapp:register')
        return redirect('storeapp:login')
    return render(request, 'register.html')


def afterlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('storeapp:afterlogin')
        else:
            messages.info(request, 'Invalid credential')
            return redirect('storeapp:login')
    return render(request, 'afterlogin.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def fill_the_form(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        dob = request.POST.get('dob','')
        age = request.POST.get('age','')
        genders = request.POST.get('genders','')
        pno = request.POST.get('pno','')
        mail = request.POST.get('mail','')
        address = request.POST.get('address','')
        department = request.POST.get('department','')
        cources = request.POST.get('courses','')
        purpose = request.POST.get('purpose','')
        materials = request.POST.get('materials','')
        store = Store(name=name, dob=dob, age=age, genders=genders, pno=pno, mail=mail, address=address, department=department,
                      cources=cources, purpose=purpose, materials=materials)
        store.save()
        # messages.info(request,'order placed')
    return render(request, 'fill_the_form.html')
