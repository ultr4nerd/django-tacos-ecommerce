"""Tacos app models"""

from django.contrib.auth.models import User
from django.db import models


class Taco(models.Model):
    """Taco model"""
    name = models.CharField('Nombre', max_length=15)
    TORTILLAS_CHOICES = (
        ('maiz', 'Tortilla de Maíz'),
        ('azul', 'Tortilla Azul'),
        ('taquera', 'Tortilla Taquera'),
        ('harina', 'Tortilla Harina'),
        ('arabe', 'Tortilla Árabe'),
    )
    tortilla = models.CharField(
        verbose_name='Tortilla',
        max_length=7,
        choices=TORTILLAS_CHOICES
    )
    price = models.DecimalField('Precio', max_digits=5, decimal_places=2)
    image = models.URLField('URL de la imagen')

    def __str__(self):
        return self.name + ' - $' + str(self.price)


class Cart(models.Model):
    """Shopping Cart model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.DecimalField(
        verbose_name='Total',
        max_digits=7,
        decimal_places=2,
        blank=True,
        default=0
    )

    def __str__(self):
        return f'{self.user.username} - ${self.total}'


class Order(models.Model):
    """Taco order"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    taco = models.ForeignKey(Taco, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Cantidad')
    subtotal = models.DecimalField(
        verbose_name='Subtotal',
        max_digits=7,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.taco.name} - ${self.subtotal}'
