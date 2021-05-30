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
    # comment_set : FK를 설정하면 Django에서 자동으로 만들어주는 클래스 속성
    # Blog 객체에 연결된 Comment 객체들에 접근할 수 있다
    # .all()을 하면 Blog 객테에 연결된 모든 Comment 객체들을 가져온다

    # 글들을 모두 가져오기 위해 comments라는 변수에 담아줌

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

        # 수정한 글을 저장
        blog_object.save()

        #redirect를 이용해 /blog/id 로 페이지의 url이동
        #id는 int형이므로 str로 형변환
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
        # blog_object의 comment를 생성
        # Comment 클래스의 멤버 변수는 body 하나 있으므로 create로 값 설정
    return redirect('/blog/'+str(id))