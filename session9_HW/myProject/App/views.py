from django.shortcuts import render, redirect
from .models import visitorLog,songRequest,Comments 
# Create your views here.

def home(request):
    visitorlogs = visitorLog.objects.all()
    return render(request, 'home.html',{'visitorlogs' : visitorlogs})

def visitorlog_create(request):
    if request.method == "POST":
        new_log = visitorLog.objects.create(
            visitorName = request.POST["visitorName"],
            title = request.POST["title"],
            visitorLog = request.POST["visitorLog"],
            visitedDate = request.POST["visitedDate"],
        )
        return redirect('visitorlog_detail', new_log.pk)
    return render(request, 'visitorlog_create.html')

def visitorlog_detail(request, log_pk):
    post_log = visitorLog.objects.get(pk = log_pk)
    if request.method == "POST":
        commentContent = request.POST["commentContent"]
        Comments.objects.create(
            commentContent = commentContent,
            visitorlog = post_log
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
            userName = request.POST["userName"]
        )
        return redirect('home')
    return render(request, 'songrequest.html')


def edit(request, log_pk):
    posted_log = visitorLog.objects.get(pk = log_pk)
    if request.method == "POST":
        edited_log = visitorLog.objects.filter(pk = log_pk).update(
            visitorName = request.POST["visitorName"],
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


