from django.urls import path
from .views import cart_add, cart_detail, cart_remove

app_name = "cart"

urlpatterns = [
    path("view/", cart_detail, name='cart_detail'),
    path("add/<int:pk>", cart_add, name='cart_add'),
    path("remove/<int:pk>", cart_remove, name='cart_remove'),
]


# app_name = "boardgames"
#
# urlpatterns = [
#     path("", index, name="index"),
#     path("list/", BoardgameListView.as_view(), name="boardgame_list"),
#     path("cathegory/", CathegorylistView.as_view(), name="cathegory_list"),
#     path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
# ]