from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=2048)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Active(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=2048)

    def __str__(self):
        return self.name


class Supplement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    url = models.URLField(max_length=2048)

    def __str__(self):
        return self.name


class Content(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    active = models.ForeignKey(Active, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    dose = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.supplement.name}: {self.active.name} ({self.dose} {self.unit.name})"


class ShoppingItem(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.price
