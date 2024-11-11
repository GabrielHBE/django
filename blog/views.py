from django.shortcuts import render
from django.http import Http404
from typing import Any
# Create your views here.

from blog.data import posts


def blog(request):

    

    contexto = {
        'text': 'to no blog',
        'posts': posts
    }

    return render(
        request=request,
        template_name='blog/index.html',
        context=contexto
    )

def exemplo(request):

    contexto = {
        'text': 'to no exemplo'
    }

    return render(
        request=request,
        template_name='blog/exemplo.html',
        context=contexto
    )

def post(request, post_id):

    found_post:dict[str,Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('N achou o post')

    context = {
        #'posts': posts,
        'post' : found_post,
        'title': f'{found_post['title']} - '
    }

    return render(request,'blog/post.html',context)
