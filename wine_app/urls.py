from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new_project/", views.new_project, name="new_project"),
    path("projects/", views.projects, name="projects"),

    # path("projects/", views.project_list, name="project_list"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/<int:project_id>/delete/", views.delete_project, name="delete_project"),
    
    # დამატებული ბილიკები
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
]
