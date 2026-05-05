from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("login/", views.WineLoginView.as_view(), name="login"),
    path("logout/", views.WineLogoutView.as_view(), name="logout"),
    path("projects/", views.project_list, name="project_list"),
    path("projects/new/", views.project_create, name="project_create"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/<int:pk>/edit/", views.project_update, name="project_update"),
    path("projects/<int:pk>/delete/", views.project_delete, name="project_delete"),
    path("projects/<int:pk>/entries/new/", views.entry_create, name="entry_create"),
    path("projects/<int:pk>/entries/<int:entry_pk>/delete/", views.entry_delete, name="entry_delete"),
]
