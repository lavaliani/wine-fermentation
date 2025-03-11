from django.urls import path
from .views import home, register, login_view, projects, new_project, project_detail, delete_project

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("projects/", projects, name="projects"),
    path("projects/new/", new_project, name="new_project"),
    path("projects/<int:project_id>/", project_detail, name="project_detail"),
    path("projects/<int:project_id>/delete/", delete_project, name="delete_project"),
]
