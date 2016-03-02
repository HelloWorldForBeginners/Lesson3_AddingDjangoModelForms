from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import *


def index(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            form = BlogForm()

    else:
        form = BlogForm()

    posts = Blog.objects.all()

    return render_to_response('myapp/index.html', {'form': form, 'posts': posts}, context_instance=RequestContext(request))
