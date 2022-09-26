from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import Todo
# Create your views here.
def home(request):
    # todolist = Todo.objects.all()
    # todolist = Todo.objects.order_by('-id')
    # context = {'todolist': todolist}
    # return render(request, 'main/home.html', context)
    return render(request, 'main/home.html')

@csrf_exempt
def get_todo_notFinished(request):
    todolist = list(Todo.objects.filter(done = False).order_by('-id').values()) #done == False인 todo를 찾고 id의 역순으로 정렬, json 변환 시 에러 피하기 위해 values() 사용 
    print(todolist)
    context = {'todolist': todolist}
    print(context)
    return HttpResponse(json.dumps(context, default=str)) #datetime은 그냥 넘기면 오류 발생하므로 string으로 변경

@csrf_exempt
def get_todo_finished(request):
    todolist = list(Todo.objects.filter(done = True).order_by('-id').values()) #done == True인 todo를 찾고 id의 역순으로 정렬, json 변환 시 에러 피하기 위해 values() 사용 
    print(todolist)
    context = {'todolist': todolist}
    print(context)
    return HttpResponse(json.dumps(context, default=str)) #datetime은 그냥 넘기면 오류 발생하므로 string으로 변경

@csrf_exempt
def new_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        new_todo=Todo.objects.create(
            content=data["content"],
            done=data["done"],
        )
        context = {
            'result': data,
        }
        print(new_todo)
        return HttpResponse(json.dumps(context))

@csrf_exempt
def delete_todo(request):
    data = json.loads(request.body)
    context = {
        'result': 'not found'
    }
    todo = Todo.objects.filter(id=data.get('id'))
    if todo is not None:
        todo.delete()
        context = {
            'result': 'done'
        }
        return HttpResponse(json.dumps(context))
    return HttpResponse(json.dumps(context))

@csrf_exempt
def check(request):
    data = json.loads(request.body)
    context = {
        'result': 'not found'
    }
    todo = Todo.objects.filter(id=data.get('id'))
    if todo is not None:
        todo.update(done= data['done'])
        context = {
            'result': 'done'
        }
        return HttpResponse(json.dumps(context))
    return HttpResponse(json.dumps(context))