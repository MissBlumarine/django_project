from django.urls import path
from .views import index, details, BoardgameListView, BoardgameDetailView, CathegorylistView

app_name = "boardgames"

urlpatterns = [
    path("", index, name="index"),
    path("list/", BoardgameListView.as_view(), name="boardgame_list"),
    path("cathegory/", CathegorylistView.as_view(), name="cathegory_list"),
    path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
]