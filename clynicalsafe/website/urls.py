from django.urls import path
from . import views


urlpatterns = [
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("blog.html", views.blog, name="blog"),
    path("contact.html", views.contact, name="contact"),
    path("Department.html", views.Department, name="Department"),
    path("Doctors.html", views.Doctors, name="Doctors"),
    path("elements.html", views.elements, name="elements"),
    path("main.html", views.main, name="main"),
    path("single-blog.html", views.single_blog, name="single_blog"),
]
