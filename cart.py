from django.shortcuts import render
from catalog.models import Flower
from django.http.request import HttpRequest


def render_with_cart(request: HttpRequest, template_name: str, context: dict=None) -> HttpRequest:
    items_id = request.session.get('cart')
    try:
        count_items = len(list(Flower.objects.get(id=item_id) for item_id in items_id))
    except BaseException as e:
        print(e)
        count_items = 0
        
    if not context:
        context = {'count_items': count_items} 
    
    if isinstance(context, dict):
        context['count_items'] = count_items
        
    print(context)
    return render(request, template_name, context)