from django.shortcuts import redirect, render
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def loginForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('err')
        user =authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('products')
    return render(request,'users/loginForm.html')