from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.http.request import HttpRequest

User = get_user_model()

def password_validator(password: str) -> str | None:
    if len(password) < 8:
        return "Password must contain at least 8 characthers"
    

def log_in(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("main")
    
    error = None
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('main')
        
        error = "Incorrect username or password!"
     
    return render(request, "authorize/login.html", {"error": error})    


def sign_up(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("main")
    
    if request.method == "GET":
        return render(request, "authorize/signup.html")
    
    elif request.method == "POST":
        error = None
    
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        error = password_validator(password)
                
        if User.objects.filter(username=username).exists():
            error = "Username already taken!"

        if error:
            return render(request, "authorize/signup.html", {'error': error})
        
        
        user = User.objects.create_user(
            first_name=first_name,
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()
        login(request, user)
        
        return redirect('main')


