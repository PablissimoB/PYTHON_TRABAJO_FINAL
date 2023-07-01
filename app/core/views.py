from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Experience
from .models import Article
from .models import Work

def presentation(request):
    return render(request, "index.html")

def error(request, exception):
    return render(request, "error.html")

def my_work(request):
    work_list = Work.objects.all()
    return render(request, "my_work.html", {"work_list": work_list})

def articles(request):
    articles_list = Article.objects.all()
    return render(request, "articles.html", {"articles_list": articles_list})

def experience(request):
    experience_list = Experience.objects.all()
    return render(request, "experience.html",{"experience_list": experience_list})

def form_articles(request):
    articles_list = Article.objects.all()
    return render(request, "form_articles.html", {"articles_list": articles_list})

def form_experience(request):
    experience_list = Experience.objects.all()
    return render(request, "form_experience.html",{"experience_list": experience_list})

def form_my_work(request):
    work_list = Work.objects.all()
    return render(request, "form_my_work.html", {"work_list": work_list})

@login_required
def menu(request):
    return render(request, "menu.html")

@login_required
def add_article(request):
    if request.method == 'POST':
        name=request.POST['articles_name']
        text=request.POST['articles_text']

        article =  Article.objects.create(articles_name=name,
                                          articles_text=text)
        return render(request, "success.html")
    else: return render(request, "error.html")

@login_required
def add_experience(request):
    if request.method == 'POST':
        name=request.POST['experience_name']
        institution=request.POST['experience_institution']

        article =  Experience.objects.create(experience_name=name,
                                             experience_institution=institution)
        return render(request, "success.html")
    else: return render(request, "error.html")

@login_required
def add_work(request):
    if request.method == 'POST':
        name=request.POST['work_name']
        url=request.POST['work_url']

        article =  Work.objects.create(work_name=name,
                                       work_url=url)
        return render(request, "success.html")
    else: return render(request, "error.html")

@login_required
def edit_experience(request, id):
    experience_list = Experience.objects.filter(id=id)
    return render(request, "edit_experience.html",{"experience_list": experience_list})

@login_required
def update_experience(request):
        experience_id=request.POST['experience_id']
        name=request.POST['experience_name']
        institution=request.POST['experience_institution']

        experience =  Experience.objects.get(id=experience_id)
        experience.experience_name = name
        experience.experience_institution = institution
        experience.save()

        messages.success(request, 'Experiencia actualizada')

        return redirect('/menu/form_experience/')

def end_session (request):
    logout(request)
    return redirect('/')