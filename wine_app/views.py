from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Project
from datetime import datetime

def home(request):
    return render(request, "wine_app/home.html")

def register(request):
    return render(request, "wine_app/register.html")

def login_view(request):
    return render(request, "wine_app/login.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "wine_app/projects.html", {"projects": projects})

def new_project(request):
    if request.method == "POST":
        project_name = request.POST.get("project_name", "").strip()
        grape_type = request.POST.get("grape_type", "").strip()
        sugar = request.POST.get("sugar", "").strip()
        brix = request.POST.get("brix", "").strip()
        ph = request.POST.get("ph", "").strip()
        acidity = request.POST.get("acidity", "").strip()
        harvest_date = request.POST.get("harvest_date", "").strip()
        wine_style = request.POST.get("wine_style", "").strip()

        # სავალდებულო ველები
        if not (project_name and grape_type and sugar):
            error = "გთხოვთ შეავსოთ აუცილებელი ველები: პროექტის სახელი, ყურძნის ტიპი და შაქარი."
            return render(request, "wine_app/new_project.html", {"error": error})

        # თუ არის harvest_date, დავამოწმოთ ფორმატი (მაგ: YYYY-MM-DD)
        parsed_harvest_date = None
        if harvest_date:
            try:
                parsed_harvest_date = datetime.strptime(harvest_date, "%Y-%m-%d").date()
            except ValueError:
                error = "არასწორი თარიღის ფორმატი. გამოიყენეთ: YYYY-MM-DD"
                return render(request, "wine_app/new_project.html", {"error": error})

        # ციფრული ველების გადაკეთება თუ საჭიროა (brix, ph, acidity)
        def to_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return None

        brix_val = to_float(brix)
        ph_val = to_float(ph)
        acidity_val = to_float(acidity)

        Project.objects.create(
            project_name=project_name,
            grape_type=grape_type,
            sugar=sugar,
            brix=brix_val,
            ph=ph_val,
            acidity=acidity_val,
            harvest_date=parsed_harvest_date,
            wine_style=wine_style if wine_style else None,
        )
        return redirect("projects")

    return render(request, "wine_app/new_project.html")

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "wine_app/project_detail.html", {"project": project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    return render(request, "wine_app/confirm_delete.html", {"project": project})
