"""
URL configuration for zakwieciscie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import main.views
import contacts.views
import authorize.views
import catalog.views
import order.views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", main.views.main, name='main'),
    path("contacts/", contacts.views.contacts, name='contacts'),
    
    path("signup/", authorize.views.sign_up, name='signup'),
    path("login/", authorize.views.log_in, name='login'),
    
    path("flowers/", catalog.views.flowers_catalog, name='flowers_catalog'),
    path("item/<int:item_id>", catalog.views.item, name='item'),
    path("add_to_cart/<int:item_id>", catalog.views.add_to_cart, name="add_to_cart"),
    path("add_to_favs/<int:item_id>", catalog.views.add_to_favs, name="add_to_favs"),
    
    path("cart/", order.views.cart, name='cart')
    # path("favs/", order.views.favs, name='favs')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

