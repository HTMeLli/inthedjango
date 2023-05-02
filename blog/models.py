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


class Connection(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ActiveIngredient(models.Model):
    name = models.CharField(max_length=200)
    connection = models.ManyToManyField(Connection, null=True, blank=True)
    # interactons = many to many with self powered by chatGPT ;-)
    interactions = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Trace(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpecialLabel(models.Model):
    name = models.CharField(max_length=200)

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
    traces = models.ManyToManyField(Trace, blank=True)
    special_labels = models.ManyToManyField(SpecialLabel, blank=True)

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


class Shop(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=2048)
    min_order_value_free_shipping = models.DecimalField(
        max_digits=20, decimal_places=2)
    shipping_price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    supplement = models.ForeignKey(Supplement, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_url = models.URLField(max_length=2048)

    def __str__(self):
        return self.product_url


class Discount(models.Model):
    UNITS = (
        ('shipping', 'Free Shipping'),
        ('discount', 'Euro Price discount'),
        ('2F1', 'Two for One'),
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    affiliate = models.BooleanField(default=False)
    discount_code = models.CharField(max_length=200, blank=True)
    discount_value = models.DecimalField(max_digits=19, decimal_places=2)
    discount_unit = models.CharField(max_length=100, choices=UNITS)
    valid_from = models.DateField(null=True, blank=True)
    valid_until = models.DateField(null=True, blank=True)
    min_order_value = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True)
    discount_url = models.URLField(max_length=2048, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    item = models.ManyToManyField(ShoppingItem, null=True, blank=True)

    def __str__(self):
        return self.name


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
