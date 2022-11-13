from django.urls import path
from .views import index, details, BoardgameListView, BoardgameDetailView, CathegoryListView, \
    BoardgameAdventuresListView, BoardgameCompanyListView, BoardgameHardcoreListView, BoardgameEconomyListView, \
    BoardgameChildListView, BoardgameBrodilkiListView, BoardgameAdultListView, BoardgameFamilyListView, \
    BoardgameNewListView

app_name = "boardgames"

urlpatterns = [
    path("", index, name="index"),
    path("new_games/", BoardgameNewListView.as_view(), name="boardgame_new"),
    path("cathegory/adventures/", BoardgameAdventuresListView.as_view(), name="boardgame_adventures"),
    path("cathegory/company/", BoardgameCompanyListView.as_view(), name="boardgame_company"),
    path("cathegory/hardcore/", BoardgameHardcoreListView.as_view(), name="boardgame_hardcore"),
    path("cathegory/economy/", BoardgameEconomyListView.as_view(), name="boardgame_economy"),
    path("cathegory/child/", BoardgameChildListView.as_view(), name="boardgame_child"),
    path("cathegory/brodilki/", BoardgameBrodilkiListView.as_view(), name="boardgame_brodilki"),
    path("cathegory/adult/", BoardgameAdultListView.as_view(), name="boardgame_adult"),
    path("cathegory/family/", BoardgameFamilyListView.as_view(), name="boardgame_family"),
    path("list/", BoardgameListView.as_view(), name="boardgame_list"),
    path("cathegory/", CathegoryListView.as_view(), name="cathegory_list"),
    path("<int:pk>/", BoardgameDetailView.as_view(), name="details"),
]