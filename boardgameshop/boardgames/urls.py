from django.urls import path
from .views import index, details, BoardgameListView, BoardgameDetailView, CathegoryListView, \
    BoardgameAdventuresListView, BoardgameCompanyListView, BoardgameHardcoreListView, BoardgameEconomyListView

app_name = "boardgames"

urlpatterns = [
    path("", index, name="index"),
    path("cathegory/adventures/", BoardgameAdventuresListView.as_view(), name="boardgame_adventures"),
    path("cathegory/company/", BoardgameCompanyListView.as_view(), name="boardgame_company"),
    path("cathegory/hardcore/", BoardgameHardcoreListView.as_view(), name="boardgame_hardcore"),
    path("cathegory/economy/", BoardgameEconomyListView.as_view(), name="boardgame_economy"),
    path("list/", BoardgameListView.as_view(), name="boardgame_list"),
    path("cathegory/", CathegoryListView.as_view(), name="cathegory_list"),
    path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
]