from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.generic import ListView, DetailView


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            # order.userprofile = request.user
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         # boardgame=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


class OrderListView(ListView):
    model = Order
    context_object_name = "orders"
    queryset = (Order
                .objects
                .all()
                )
    template_name = 'orders/order/order_list.html'


def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order/order_list.html',
                  {'orders': orders, })


def no_orders(request):
    return render(request, 'orders/order/no_list.html')
