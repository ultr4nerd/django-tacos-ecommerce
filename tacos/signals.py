"""Taco app signals"""

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order

@receiver(pre_save, sender=Order)
def update_subtotal(sender, instance, **kwargs):
    taco_price = instance.taco.price
    quantity = instance.quantity
    instance.subtotal = taco_price * quantity
    instance.cart.total += instance.subtotal
    instance.cart.save()
