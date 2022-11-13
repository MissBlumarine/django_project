from django.urls import path
from . import views
from .views import OrderListView

app_name = "orders"

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('created_orders/', OrderListView.as_view(), name='order_list'),
    # path('created_orders/<pk:int>/', views.order_create, name='order_detail'),
]
