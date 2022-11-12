from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from boardgames.models import Boardgame
from .models import Cart
from .forms import CartAddProductForm
from django.views.generic import DetailView


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Boardgame, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(boardgame=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')
    # return render(request=request, template_name="cart/cart_detail.html")


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Boardgame, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
    # return render(request=request, template_name='cart/cart_detail.html')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


class CartDetailView(DetailView):
    model = Cart
