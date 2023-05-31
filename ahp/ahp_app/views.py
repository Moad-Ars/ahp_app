from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    form = UserCreationForm()

    if request.method == 'GET':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'ahp/register.html', context)

def login(request):
    context = {}
    return render(request, 'ahp/login.html', context)

def home(request):
    return render(request, 'ahp/dashboard.html')

def ahp_calculator(request):
    return render(request, 'ahp/ahp_calculator.html')

def user(request):
    return render(request, 'ahp/user.html')
