"""Taco app view"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView

from .models import Taco, Order


class IndexView(TemplateView):
    """Index view"""
    template_name = 'tacos/index.html'


class MenuView(ListView):
    """Lists all tacos"""
    model = Taco
    template_name = 'tacos/menu.html'


@login_required
def order(request, pk):
    """Order view"""
    if request.method == 'GET':
        taco = get_object_or_404(Taco, pk=pk)
        return render(request, 'tacos/detail.html', {'taco': taco})
    else:
        cart = request.user.cart
        taco = get_object_or_404(Taco, pk=pk)
        quantity = int(request.POST.get('quantity'))
        order = Order.objects.create(cart=cart, taco=taco, quantity=quantity)
        messages.success(
            request, f'Se ha añadido la orden al carrito ({order})'
        )
        return redirect('tacos:list')


@login_required()
def cart(request):
    """Shopping cart summary"""
    orders = request.user.cart.order_set.all()
    return render(request, 'tacos/cart.html', {'orders': orders})
