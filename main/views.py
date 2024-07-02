from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def main(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user.get_username())
    return render(request, 'main/index.html')