from django.shortcuts import render, redirect
from .models import Major, Subject
from django.views.generic import CreateView, UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy
# Create your views here.

class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'home.html', {'majors' : majors, 'subjects' : subjects})

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')

def computer(request):
    subjects= Subject.objects.filter(Subject_major__name='컴퓨터학과')
    return render(request, 'computer.html', {'subjects' : subjects})

class EditSubjectView(UpdateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'EditSubject.html'
    success_url = reverse_lazy('home')

def delete_subject(request, post_pk):
    post = Subject.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def education(request):
    subjects= Subject.objects.filter(Subject_major__name='교육학과')
    return render(request, 'education.html', {'subjects' : subjects})

class EditMajorView(UpdateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'EditMajor.html'
    success_url = reverse_lazy('home')

def delete_major(request, post_pk):
    post = Major.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def major_list(request, major_name):
    subjects = Subject.objects.filter(Subject_major__name=major_name)
    return render(request, 'major_list.html', {'subjects' : subjects})    




