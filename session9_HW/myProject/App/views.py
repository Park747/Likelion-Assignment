from django.shortcuts import render, redirect
from .models import visitorLog,songRequest,Comments,User
from django.contrib.auth.decorators import login_required 
from django.contrib import auth
# Create your views here.

def home(request):
    visitorlogs = visitorLog.objects.all()
    return render(request, 'home.html',{'visitorlogs' : visitorlogs})

@login_required(login_url="/login")
def visitorlog_create(request):
    if request.method == "POST":
        new_log = visitorLog.objects.create(
            visitorName = request.user,
            title = request.POST["title"],
            visitorLog = request.POST["visitorLog"],
            visitedDate = request.POST["visitedDate"],
        )
        return redirect('visitorlog_detail', new_log.pk)
    return render(request, 'visitorlog_create.html')

@login_required(login_url="/login")
def visitorlog_detail(request, log_pk):
    post_log = visitorLog.objects.get(pk = log_pk)
    post_log.numberView += 1
    post_log.save()
    if request.method == "POST":
        commentContent = request.POST["commentContent"]
        Comments.objects.create(
            commentContent = commentContent,
            visitorlog = post_log,
            commentName = request.user
        )
        return redirect('visitorlog_detail', post_log.pk)
    return render(request, 'visitorlog_detail.html', {'post_log' : post_log})

def showroom(request):
    return render(request, 'showroom.html')

def piano(request):
    return render(request, 'piano.html')

def songrequest(request):
    if request.method =="POST":
        new_request = songRequest.objects.create(
            songName = request.POST["songName"],
            userName = request.POST["userName"],
            requestName = request.POST["requestName"]
        )
        return redirect('home')
    return render(request, 'songrequest.html')


def edit(request, log_pk):
    posted_log = visitorLog.objects.get(pk = log_pk)
    if request.method == "POST":
        edited_log = visitorLog.objects.filter(pk = log_pk).update(
            visitorName = request.user,
            title = request.POST["title"],
            visitorLog = request.POST["visitorLog"],
            visitedDate = request.POST["visitedDate"],
        )
        return redirect('visitorlog_detail', posted_log.pk)

    return render(request, 'edit.html' , {'posted_log' : posted_log})

def delete(request, log_pk):
    delete_log = visitorLog.objects.get(pk = log_pk)
    delete_log.delete()
    return redirect('home')

def editcomment(request, log_pk, comment_pk):
    comment = Comments.objects.filter(pk = comment_pk)
    post_log = visitorLog.objects.get(pk = log_pk)
    if request.method == "POST":
        comment.update(
            commentName = request.user,
            commentContent = request.POST['commentContent'],
            visitorlog = post_log
        )
        return redirect('visitorlog_detail', post_log.pk)
    return render(request, 'editcomment.html' , {'post_log' : post_log})

def deletecomment(request, log_pk, comment_pk):
    comment = Comments.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('visitorlog_detail', log_pk)

def signup(request):
    if request.method == "POST":
        if request.POST['userPWD'] == request.POST['userPWD2']:
            user = User.objects.create_user(
                username = request.POST['userID'],
                password = request.POST['userPWD']
            )
            auth.login(request, user)
            return redirect('home')
        return render(request,'signup.html')
    return render(request,'signup.html')
    

def login(request):
    if request.method == "POST":
        username = request.POST['userName']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")




    
