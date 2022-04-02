from re import I
from django.shortcuts import render
from django.http import HttpResponse

from .models import PostModel


def index(request):
    post = PostModel.objects.order_by("-pub_date")[:10]
    context = {
        "posts": post
    }
    return render(request, "index.html", context)
