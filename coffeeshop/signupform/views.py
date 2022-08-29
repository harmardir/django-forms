from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import NameForm

def Home(request):
    return render(request,"signupform/home.html")

def Thanks(request):
    return render(request,"signupform/thanks.html")
    
    
def Signup(request):
    if request.method == 'POST':
        # process the form data
        form = NameForm(request.POST)
    
        if form.is_valid():
            # validate the data
            # ...
            # redirect to new URL
            form.save()
            return HttpResponseRedirect('thanks')
    
    else:
        # create a blank form
        form = NameForm()
    return render(request,"signupform/signup.html", {'form': form})
