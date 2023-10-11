from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_portfolio>/portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contact, name="contact"),
    path("team", views.team, name="team"),
    path("asanka", views.asanka, name="asanka")

]