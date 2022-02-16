from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("<int:id>/", views.IndividualPostView, name="focus-post")
]