from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, TimeStampModel
# Create your views here.


def home(request):
    blog_objects = Blog.objects.all()
    return render(request, 'home.html', {'data': blog_objects})

def post_read(request, id):
    blog_object = get_object_or_404(Blog, pk=id)
    # Comment 가져오도록 추가
    comments = blog_object.comment_set.all()

    return render(request, 'post_read.html', {'data': blog_object, 'comments' : comments})

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

def post_edit(req, id) :
    blog_object = get_object_or_404(Blog, pk = id)

    # 수정한 글을 저장하기 위해 함수 추가 작업
    if req.method == "POST" :
        blog_object.title = req.POST['title']
        blog_object.body = req.POST['body']

        blog_object.save()

        return redirect('/blog/'+str(id))

    return render(req, 'post_edit.html', {'data' : blog_object})

def post_delete(req, id) :
    blog_object = get_object_or_404(Blog, pk = id)
    blog_object.delete()

    return redirect('/')

# Comment 등록
def comment_create(req, id) :
    if req.method == 'POST':
        blog_object = get_object_or_404(Blog, pk = id)
        blog_object.comment_set.create(body = req.POST['comment'])

    return redirect('/blog/'+str(id))