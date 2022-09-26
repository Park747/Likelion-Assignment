from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
import datetime


def home(request):
    posts = Post.objects.order_by('deadline')
    today = datetime.date.today()
    return render(request, 'home.html', {'posts' : posts, 'today' : today})

def new(request):      
    if request.method == 'POST':    #어떠한 주소로 단순 접근의 요청은 POST 아님. form을 통한 요청이 POST임. ex. 그냥 링크를 클릭해서 url로 갔을떄? POST가 아니라 GET요청임.
        new_post = Post.objects.create(
        title = request.POST['title'],   #html에 있는 name을 key로 값을 꺼냄, 요청값이 POST안에 딕셔너리 형태로 저장되어 있음       
        content = request.POST['content'],
        deadline = request.POST['deadline']
        )
        return redirect('detail', new_post.pk) #new_post의 pk값을 경로변수로 넣어준것임
    return render(request,'new.html')

def detail(request, post_pk): #views에서 또 urls.py에서 넘겨받은 경로변수를 고대로 파라미터로 받는다. 따라서 home.html에서 넘겨준 post.pk의 값이 여기 인자로 들어오게 되는것. 그래서 get으로 pk값을 필터한다.
    post=Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post' : post} ) #post는 컨택스트 변수, html에 매핑되어 들어감.

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        updated_post = Post.objects.filter(pk=post_pk).update(   #edit로 넘어갈때 요청이 POST일 경우 / 그냥 GET으로 edit으로 갈 경우로 나뉨.
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline']
        )
        return redirect('detail' , post_pk)

    return render(request, 'edit.html' , {'post' : post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')



