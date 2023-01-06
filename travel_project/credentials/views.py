from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        user_name = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=user_name, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mail_id = request.POST['mail_id']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_pw']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('credentials:registration')
            elif User.objects.filter(email=mail_id).exists():
                messages.info(request, 'mail id taken')
                return redirect('credentials:registration')
            else:
                user = User.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=mail_id,
                                            password=password)
            user.save()
            print('user created')
            return redirect('credentials:login')
        else:
            print('Password not matching')
            messages.info(request, 'Password not matching')
            return redirect('credentials:registration')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')