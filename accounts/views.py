from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login , authenticate
from .models import Profile
from django.http import HttpResponse
from .forms import SignupForm
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponse('registred sucessfully')
        else:
            form = SignupForm()
    
        return render(request,'registration/signup.html',{'form': form})

def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile':profile}
    return render(request,'profile.html',context)
