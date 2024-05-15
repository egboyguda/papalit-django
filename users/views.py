from django.shortcuts import render

# Create your views here.
def loginForm(request):
    return render(request,'users/loginForm.html')