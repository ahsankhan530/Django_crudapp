from django.shortcuts import render,redirect
from .models  import registrations
from crudapp.forms import registrationForm
def emp (request):
    if request.method=='POST':
        form=registrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=registrationForm()
        return render(request,'index.html',{'form':form})

def show(request):
    registration=registrations.objects.all()
    return render(request,'show.html',{'registration':registration})