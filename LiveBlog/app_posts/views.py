from re import I
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import PostModel, GroupModel


def index(request):
    post = PostModel.objects.order_by("-pub_date")[:10]
    context = {
        "posts": post,
    }
    return render(request, "index.html", context)

def group_post(request, slug):
    group = get_object_or_404(GroupModel, slug=slug)
    posts = PostModel.objects.filter(group=group).order_by("-pub_date")[:10]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "group.html", context)
