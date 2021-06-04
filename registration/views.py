from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserForm
from django.contrib.auth import login, authenticate


# Create your views here.
    
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:home')
    else:
        form = UserForm()
    
    return render(request,'registration/reg_index.html',{'form':form})


def login(request):
    # form = UserForm()
    if request.method == "POST":
        username = request.POST.get('username', False)
        # username = request.POST['username']
        # password = request.POST['password']
        password = request.POST.get('password', False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect(reverse('register_login_landing'))
            redirect('polls:home')
        else:
            return "You have provided wrong infromation"

    return render(request, 'registration/login.html', {})


