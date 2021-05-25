from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, TimeStampModel
# Create your views here.


def home(request):
    blog_objects = Blog.objects.all()
    return render(request, 'home.html', {'data': blog_objects})

def post_read(request, id):
    blog_object = get_object_or_404(Blog, pk=id)
    return render(request, 'post_read.html', {'data': blog_object})

def post_create(request):
    if request.method == 'POST':
        blog_object = Blog()
        blog_object.title = request.POST['title']
        blog_object.body = request.POST['body']
        blog_object.save()
        return redirect('/blog/'+str(blog_object.id))
        
    return render(request, 'post_create.html')

def post_update(request) :
    return render(request, 'post_update.html')