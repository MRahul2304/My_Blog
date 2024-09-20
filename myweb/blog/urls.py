from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("post/<str:slug>", views.details, name="details"),
    path("new_url", views.new_url_redirect, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url"),
]
