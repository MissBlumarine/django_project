from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import add_item_to_cart

app_name = "cart"

urlpatterns = [
    path("view/", TemplateView.as_view(template_name='cart/cart.html'), name="cart_view"),
    path('add/<int:pk>', add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
]