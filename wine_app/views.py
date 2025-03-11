from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project

def home(request):
    return render(request, "wine_app/home.html")  # დარწმუნდი, რომ ეს ფაილი არსებობს

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

        # ცარიელი ველების თავიდან აცილება
        if project_name and grape_type and sugar:
            Project.objects.create(
                project_name=project_name,
                grape_type=grape_type,
                sugar=sugar,
                brix=brix if brix else None,
                ph=ph if ph else None,
                acidity=acidity if acidity else None,
                harvest_date=harvest_date if harvest_date else None,
                wine_style=wine_style if wine_style else None,
            )
            return redirect("projects")  # აქ `projects` სია გადაგიყვანს

    return render(request, "wine_app/new_project.html")

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "wine_app/project_detail.html", {"project": project})

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":  # უსაფრთხოების გამო, წაშლა მხოლოდ POST-ით
        project.delete()
        return redirect("projects")  # დარწმუნდი, რომ "projects" URL რეგისტრირებულია  

    return render(request, "wine_app/confirm_delete.html", {"project": project})
