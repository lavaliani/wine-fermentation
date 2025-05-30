from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not (username and email and password1 and password2):
            error = "გთხოვთ შეავსოთ ყველა ველი."
            return render(request, "wine_app/register.html", {"error": error})

        if password1 != password2:
            error = "პაროლები არ ემთხვევა."
            return render(request, "wine_app/register.html", {"error": error})

        if User.objects.filter(username=username).exists():
            error = "მომხმარებლის სახელი დაკავებულია."
            return render(request, "wine_app/register.html", {"error": error})

        if User.objects.filter(email=email).exists():
            error = "ეს ელ-ფოსტა უკვე გამოყენებულია."
            return render(request, "wine_app/register.html", {"error": error})

        # შექმენით მომხმარებელი
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # ავტომატურად შეყვანა (login) რეგისტრაციის შემდეგ
        login(request, user)

        return redirect("home")

    return render(request, "wine_app/register.html")
