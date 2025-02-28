from django.shortcuts import render, redirect
from.forms import DataForm, ContactForm
from . import models 
from django.contrib import messages



#home page
def home(request):
    updates=models.Announcements.objects.all()
    admin=models.Administration.objects.all()
    return render(request,"home.html",{"updates":updates,"admin":admin})

#application
def application(request):
    if request.method=="POST":
        form=DataForm(request.POST or None,request.FILES)
        #incase form is validates
        if form.is_valid():
            form.save()
            messages.success(request,"You have successfully Resgistered.")
            #clear the form
            form=DataForm()
            return render(request,"application.html",{'form':form})
        else:
            form=DataForm()
            return render(request,"application.html",{'form':form})
    else:
            form=DataForm()
            return render(request,"application.html",{'form':form})




#login
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the MySQL database
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')  # Redirect to prevent form resubmission
        else:
            messages.error(request, 'Error sending message. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'login.html', {'form': form})