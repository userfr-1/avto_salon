from django.db import models

class BaseClass(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Brand(BaseClass):
    title = models.CharField(max_length=100)
    context = models.TextField()

    def __str__(self):
        return self.title

class Autosalon(BaseClass):
    title = models.CharField(max_length=255)
    context = models.TextField()
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.title

class Car(BaseClass):
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.DateField()
    color = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    salon = models.ForeignKey(Autosalon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} - {self.year}"


# Create your models here.
