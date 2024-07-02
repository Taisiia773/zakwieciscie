from django.shortcuts import render
from django.http import HttpRequest
from catalog.models import *

# Create your views here.
def cart(request: HttpRequest):
    items_id = request.session.get('cart')
    cart_items = []
    total_price = 0
    
    try:
        for item_id in items_id:
            cart_items.append(Flower.objects.get(id=item_id))
    except:
        return render(request, 'order/cart.html')
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, "order/cart.html", context=context)