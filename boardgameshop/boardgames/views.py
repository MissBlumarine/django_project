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


# class BoardgameImageListView(ListView):
#     context_object_name = "boardgame_img"
#     queryset = (BoardgameImage
#                 .objects
#                 .all()
#                 )


def product_detail(request, pk, slug):
    product = get_object_or_404(Boardgame,
                                pk=pk,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'boardgames/boardgame_detail.html', {'product': product,
                                                                'cart_product_form': cart_product_form})
