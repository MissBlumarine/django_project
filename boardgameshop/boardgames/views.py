from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from .models import Boardgame, Cathegory


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


class CathegorylistView(ListView):
    context_object_name = "cathegorys"
    queryset = (Cathegory
                .objects
                .order_by("pk")
                .all()
                )
