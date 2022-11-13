from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from .models import Boardgame, Cathegory, BoardgameImage
from cart.forms import CartAddProductForm


def index(request: HttpRequest):
    context = {
        "boardgames": Boardgame.objects.order_by("pk").all()
    }
    return render(request=request, template_name="boardgames/index.html", context=context)


def details(request: HttpRequest, pk: int, slug):
    context = {
        "boardgame": get_object_or_404(Boardgame, pk=pk)
    }
    cart_product_form = CartAddProductForm()
    return render(request=request, template_name="boardgames/details.html", context=context)


# slug= {'product': product, 'cart_product_form': cart_product_form}


class BoardgameListView(ListView):
    context_object_name = "boardgames"
    queryset = (Boardgame
                .objects
                .order_by("pk")
                .all()
                )


class BoardgameDetailView(DetailView):
    model = Boardgame


class CathegoryListView(ListView):
    context_object_name = "cathegorys"
    queryset = (Cathegory
                .objects
                .order_by("pk")
                .all()
                )


class BoardgameAdventuresListView(ListView):
    context_object_name = "adventures"
    queryset = (Boardgame
                .objects
                .filter(cathegory_id=1)
                .order_by("pk")
                )


class BoardgameCompanyListView(ListView):
    context_object_name = "company"
    queryset = (Boardgame
                .objects
                .filter(cathegory_id=2)
                .order_by("pk")
                )


class BoardgameHardcoreListView(ListView):
    context_object_name = "hardcore"
    queryset = (Boardgame
                .objects
                .filter(cathegory_id=3)
                .order_by("pk")
                )


class BoardgameEconomyListView(ListView):
    context_object_name = "economy"
    queryset = (Boardgame
                .objects
                .filter(cathegory_id=4)
                .order_by("pk")
                )


def product_detail(request, pk, slug):
    product = get_object_or_404(Boardgame,
                                pk=pk,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'boardgames/boardgame_detail.html', {'product': product,
                                                                'cart_product_form': cart_product_form})
