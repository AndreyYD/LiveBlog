from django.urls import path

from .views import index, group_post


urlpatterns = [
    path("", index, name="index"),
    path("group/<slug:slug>/", group_post, name="group"),
]