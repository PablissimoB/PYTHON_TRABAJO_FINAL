from django.shortcuts import render
from .models import Experience
from .models import Article
from .models import Work

def presentation(request):
    return render(request, "index.html")

def my_work(request):
    return render(request, "my_work.html")

def articles(request):
    return render(request, "articles.html")

def experience(request):
    return render(request, "experience.html")

def form_articles(request):
    return render(request, "form_articles.html")

def form_experience(request):
    return render(request, "form_experience.html")

def form_my_work(request):
    return render(request, "form_my_work.html")

def menu(request):
    return render(request, "menu.html")

def form_add_experience(request):
    if request.method == 'POST':
        item =  Experience(experience_name=request.POST['experience_name'],experience_institution=request.POST['experience_institution'])
        item.save()
        return render(request, "success.html")
    return render(request,"form_experience.html")

def form_add_articles(request):
    if request.method == 'POST':
        item =  Article(articles_name=request.POST['articles_name'],articles_text=request.POST['articles_text'])
        item.save()
        return render(request, "success.html")
    return render(request,"form_experience.html")

def form_add_work(request):
    if request.method == 'POST':
        item =  Work(work_name=request.POST['work_name'],work_url=request.POST['work_url'])
        item.save()
        return render(request, "success.html")
    return render(request,"form_experience.html")