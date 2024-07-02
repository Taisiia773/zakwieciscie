from django.shortcuts import render
from django.http import *
from .models import *


# Create your views here.
def item(request: HttpRequest, item_id: str) -> HttpResponse:
    print(type(item_id))
    flower = Flower.objects.get(id=item_id)
    
    return render(request, "catalog/item.html", {"flower": flower})

def flowers_catalog(request: HttpRequest) -> HttpResponse:
    context = {}
    context['flowers'] = Flower.objects.all()
    
    return render(request, "catalog/flowers_catalog.html", context=context)

def add_to_cart(request: HttpRequest, item_id):
    if not request.session.get('cart'):
        request.session['cart'] = []
    
    request.session['cart'].append(str(item_id))
    request.session.modified = True
        
    print(request.session.session_key, item_id)
    print(request.session.get('cart'))
    # return render(request, "catalog/flowers_catalog.html")
    return render(request, "main/index.html")


def add_to_favs(request: HttpRequest, item_id):
    if not request.session.get('favs'):
        request.session['favs'] = []
    
    request.session['favs'].append(str(item_id))
    request.session.modified = True
        
    print(request.session.session_key, item_id)
    print(request.session.get('favs'))

    return render(request, "main/index.html")