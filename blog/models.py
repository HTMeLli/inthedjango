from django.conf import settings
from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=2048, blank=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ActiveIngredient(models.Model):
    name = models.CharField(max_length=200)
    # interactons = many to many with self

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=2048)
    min_order_value_free_shipping = models.DecimalField(
        max_digits=20, decimal_places=2)
    shipping_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Supplement(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    active_ingredients = models.ManyToManyField(
        ActiveIngredient, through="Content", blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    active_ingredient = models.ForeignKey(
        ActiveIngredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    dose = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.supplement.name}: {self.active_ingredient.name} ({self.dose} {self.unit.name})"


class ShoppingItem(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_url = models.URLField(max_length=2048)

    def __str__(self):
        return self.product_url


class Price(models.Model):
    class Tax(models.IntegerChoices):
        TAX_7 = 7
        TAX_19 = 19
        TAX_CHOICES = (
            (TAX_7, '7%'),
            (TAX_19, '19%'),
        )
    price_net = models.DecimalField(max_digits=19, decimal_places=2)
    tax = models.IntegerField(choices=Tax.choices)

    def __str__(self):
        result = self.price_net + self.price_net*self.tax/100
        return f"{result:.2f}"
