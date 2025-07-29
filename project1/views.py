from django.shortcuts import render, redirect,get_object_or_404

from .forms import AvtoSalonForms
from .models import *
def index(request):
    salon = Autosalon.objects.all()
    context = {
        'salon': salon,
        'title': 'AUTOSALON',
    }
    return render(request, 'index.html', context=context)


def add_salon(request):
    if request.method == 'POST':
        form = AvtoSalonForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AvtoSalonForms()

    return render(request, 'add_salon.html', context={'form': form})

def detail_salon(request,pk):
    salon = get_object_or_404(Autosalon,pk=pk)
    context = {
        "salon": salon

    }
    return render(request,'detail_salon.html',context=context)

def salon_cars(request,brand_pk,salon_pk):
    cars = Car.objects.filter(brand = brand_pk,salon = salon_pk)
    brand = Brand.objects.all()
    context = {
        "salon_pk": salon_pk,
        "cars":cars,
        "brand":brand
    }
    return render(request,'salon_cars.html',context)