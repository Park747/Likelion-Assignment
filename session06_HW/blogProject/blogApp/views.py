from django.shortcuts import render, redirect
from pkg_resources import PEP440Warning
from .models import Article
import datetime

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article= Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('list')
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    hobby_category = Article.objects.filter(category='hobby')
    food_category = Article.objects.filter(category='food')
    programming_category = Article.objects.filter(category='programming')
    return render(request, 'list.html', {'articles': articles, 'hobby_category' : hobby_category, 'food_category' : food_category, 'programming_category' : programming_category})
# Create your views here.
def detail(request, article_id):
    article_detail = Article.objects.get(id=article_id)
    return render(request,'detail.html' , {'article_detail' : article_detail})

def category_hobby(request):
    hobby_category = Article.objects.filter(category='hobby')
    return render(request, 'hobby.html', {'hobby_category' : hobby_category})
def category_food(request):
    food_category = Article.objects.filter(category='food')
    return render(request, 'food.html', {'food_category' : food_category})
def category_programming(request):
    programming_category = Article.objects.filter(category='programming')
    return render(request, 'programming.html', {'programming_category' : programming_category})
    
