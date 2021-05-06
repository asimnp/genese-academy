from django.db import models
from django.core.exceptions import ValidationError


class DateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


def check_product_price_not_negative_or_zero(value):
    if value < 0 or value == 0:
        raise ValidationError('Price should not be negative or zero.')


class Product(DateTimeModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[check_product_price_not_negative_or_zero])

    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True, related_name='category')

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.name
