from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .forms import NameForm , UserForm

def Home(request):
    return render(request,"signupform/home.html")

def Thanks(request):
    return render(request,"signupform/thanks.html")
    
    
def Signup(request):
    if request.method == 'POST':
        # process the form data
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    
    else:
        # create a blank form
        form = UserForm()
    return render(request,"signupform/signup.html", {'form': form})
