import json

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import FermentationEntryForm, GeorgianAuthenticationForm, RegisterForm, WineProjectForm
from .models import FermentationEntry, WineProject


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "wine_app/home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "რეგისტრაცია დასრულდა. ახლა შეგიძლია პირველი პროექტი შექმნა.")
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "wine_app/auth_form.html", {"form": form, "title": "რეგისტრაცია"})


class WineLoginView(LoginView):
    authentication_form = GeorgianAuthenticationForm
    template_name = "wine_app/auth_form.html"
    extra_context = {"title": "შესვლა"}


class WineLogoutView(LogoutView):
    next_page = reverse_lazy("home")


def _project_queryset(request):
    queryset = WineProject.objects.prefetch_related("entries")
    if request.user.is_authenticated:
        return queryset.filter(owner=request.user)
    return queryset.none()


@login_required
def dashboard(request):
    projects = _project_queryset(request)
    active_projects = projects.filter(is_active=True)
    latest_entries = FermentationEntry.objects.filter(project__owner=request.user).select_related("project")[:6]
    totals = {
        "projects": projects.count(),
        "active": active_projects.count(),
        "entries": FermentationEntry.objects.filter(project__owner=request.user).count(),
    }
    styles = list(projects.values("wine_style").annotate(total=Count("id")).order_by("wine_style"))
    return render(
        request,
        "wine_app/dashboard.html",
        {"projects": projects[:8], "latest_entries": latest_entries, "totals": totals, "styles": styles},
    )


@login_required
def project_list(request):
    projects = _project_queryset(request)
    return render(request, "wine_app/project_list.html", {"projects": projects})


@login_required
def project_create(request):
    if request.method == "POST":
        form = WineProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, "პროექტი შეიქმნა.")
            return redirect(project)
    else:
        form = WineProjectForm()
    return render(request, "wine_app/project_form.html", {"form": form, "title": "ახალი პროექტი"})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(_project_queryset(request), pk=pk)
    entries = project.entries.all()
    entry_form = FermentationEntryForm(initial={"measured_at": timezone.localtime().strftime("%Y-%m-%dT%H:%M")})
    chart_entries = list(entries.order_by("measured_at"))
    chart_data = {
        "labels": [timezone.localtime(entry.measured_at).strftime("%d.%m %H:%M") for entry in chart_entries],
        "temperature": [float(entry.temperature) if entry.temperature is not None else None for entry in chart_entries],
        "brix": [float(entry.brix) if entry.brix is not None else None for entry in chart_entries],
        "ph": [float(entry.ph) if entry.ph is not None else None for entry in chart_entries],
    }
    return render(
        request,
        "wine_app/project_detail.html",
        {"project": project, "entries": entries, "entry_form": entry_form, "chart_data": json.dumps(chart_data, ensure_ascii=False)},
    )


@login_required
def project_update(request, pk):
    project = get_object_or_404(_project_queryset(request), pk=pk)
    if request.method == "POST":
        form = WineProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "პროექტი განახლდა.")
            return redirect(project)
    else:
        form = WineProjectForm(instance=project)
    return render(request, "wine_app/project_form.html", {"form": form, "title": "პროექტის რედაქტირება", "project": project})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(_project_queryset(request), pk=pk)
    if request.method == "POST":
        project.delete()
        messages.success(request, "პროექტი წაიშალა.")
        return redirect("project_list")
    return render(request, "wine_app/project_confirm_delete.html", {"project": project})


@login_required
@require_POST
def entry_create(request, pk):
    project = get_object_or_404(_project_queryset(request), pk=pk)
    form = FermentationEntryForm(request.POST)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.project = project
        entry.save()
        messages.success(request, "ფერმენტაციის ჩანაწერი დაემატა.")
    else:
        messages.error(request, "ჩანაწერი ვერ დაემატა. გადაამოწმე ველები.")
    return redirect(project)


@login_required
@require_POST
def entry_delete(request, pk, entry_pk):
    project = get_object_or_404(_project_queryset(request), pk=pk)
    entry = get_object_or_404(project.entries, pk=entry_pk)
    entry.delete()
    messages.success(request, "ჩანაწერი წაიშალა.")
    return redirect(project)
