from django.shortcuts import render, redirect
from cars.models import UserDetails,Car_miles,Car_roof,Car_engine,Car_service
from cars.forms import UserModelForm
from django.contrib.auth import login
from django.urls import reverse
from cars.forms import CustomUserCreationForm
# Create your views here.

def all_cars(request):
    show_users = UserDetails.objects.all()
    return render(request,'all_cars.html', {'show_users': show_users})

def all_car_details(request,pk):
    all_details = UserDetails.objects.get(pk=pk)
    context = {
        'all_details' : all_details
    }
    return render(request,'showcars_detail.html', context)

def userDetails(request):
    form = UserModelForm()
    if request.method == 'POST':
        form = UserModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UserModelForm()
            return render(request, 'display.html', {
                'form': form
            })
    else:
        form = UserModelForm()

    return render(request, 'userdetails.html', {
        'form': form ,
    })

def update_details(request,pk):
    update_car = UserDetails.objects.get(pk=pk)
    form = UserModelForm(instance=update_car)
    if request.method == "POST":
        form = UserModelForm(request.POST,request.FILES, instance=update_car)
        if form.is_valid():
            form.save()
            return redirect('/showcars')
    context = {
        'form':form
    }
    return render(request,'update_car_details.html',context)

def delete_car(request,pk):
    item = UserDetails.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/showcars')
    context = {
        'item':item
    }
    return render(request,'delete.html',context)


def register(request):
    context = {}
    if request.method == "GET":
        form = CustomUserCreationForm
        context["registration_form"] = form
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect(reverse("cars"))
        else:
            context["registration_form"] = form

    return render(request,'users/register.html',context)
