from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('err')
            messages.error(request,"invalid username/password")
        user =authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome")
            return redirect('products')
    return render(request,'users/loginForm.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'Successfully Logout')
    return redirect('login')