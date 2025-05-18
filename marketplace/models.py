from django.db import models
from django.contrib.auth.models import AbstractUser


class Tovar(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    opicanie = models.TextField()
    date_vipuck = models.DateField()
    kolvo = models.IntegerField()
    image = models.ImageField('Изображение', upload_to='images/',
                              blank=True, null=True, default='images/default.jpg')


class Polbzovatelb(AbstractUser):
    address = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)


class Karzina(models.Model):
    tavari = models.ManyToManyField(Tovar, related_name="korzins", through="Karzina_Tovar")
    uzer = models.OneToOneField(Polbzovatelb, on_delete=models.CASCADE, related_name="korzina")


class Karzina_Tovar(models.Model):
    karzina = models.ForeignKey(Karzina, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    kolvo = models.IntegerField(default=1)