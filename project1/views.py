import io
import qrcode
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from .forms import AvtoSalonForm, CarForm
from .models import Autosalon, Brand, Car
from django.urls import reverse
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


def index(request):
    salon = Autosalon.objects.all()
    context = {'salon': salon, 'title': 'AUTOSALON'}
    return render(request, 'index.html', context)

def add_salon(request):
    if request.method == 'POST':
        form = AvtoSalonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AvtoSalonForm()
    return render(request, 'add_salon.html', {'form': form})

def detail_salon(request, pk):
    salon = get_object_or_404(Autosalon, pk=pk)
    return render(request, 'detail_salon.html', {'salon': salon})

def salon_cars(request, brand_pk, salon_pk):
    cars = Car.objects.filter(brand=brand_pk, salon=salon_pk)
    brand = Brand.objects.all()
    context = {
        "salon_pk": salon_pk,
        "cars": cars,
        "brand": brand
    }
    return render(request, 'salon_cars.html', context)

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def car_pdf(request, pk):
    car = get_object_or_404(Car, pk=pk)

    url = request.build_absolute_uri(reverse('car_pdf', args=[car.pk]))


    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # --- PDF ---
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Matnlar
    p.setFont("Helvetica-Bold", 20)
    p.drawString(70, height-70, f"{car.brand.title} {car.model}")
    p.setFont("Helvetica", 12)
    p.drawString(70, height-100, f"Yil: {car.year}")
    p.drawString(70, height-120, f"Rang: {car.color}")
    p.drawString(70, height-140, f"Narx: {car.price} $")
    p.drawString(70, height-160, f"Salon: {car.salon.title}")

    # QR code
    p.drawImage(ImageReader(qr_img), width-180, height-220, 120, 120)


    if car.image:
        p.drawImage(
            ImageReader(car.image.path),
            70, height-380, 320, 200,
            preserveAspectRatio=True, mask='auto'
        )

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{car.model}.pdf")
