from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.urls import reverse_lazy

from .models import Profile
from .models import Experience
from .models import Article
from .models import Work

from .form import ProfileEditForm, UserEditForm

def presentation(request):
    item = User.objects.all()
    profile = Profile.objects.filter(user_id=1)
    return render(request, "index.html", {"usuario": item, "profile":profile})

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

def article(request, id):
    article_list = Article.objects.filter(id=id)
    return render(request, "article.html",{"article_list": article_list})

@login_required
def edit_profile(request):
    usuario = User.objects.get(username = request.user)
    profile = Profile.objects.get(user=usuario)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            profile.imagen = form.cleaned_data["imagen"]
            profile.city = form.cleaned_data["city"]
            profile.country = form.cleaned_data["country"]
            profile.save()
    else:
        form = ProfileEditForm(
            initial ={
                'city': profile.city,
                'country':profile.country
            }
        )
    return render(request, "form_profile.html",{"profile": profile,"form": form})


@login_required
def edit_user(request):
    usuario = User.objects.get(username = request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.last_name = form.cleaned_data["last_name"]
            usuario.first_name = form.cleaned_data["first_name"]
            usuario.email = form.cleaned_data["email"]
            usuario.password = form.cleaned_data["password"]
            usuario.save()
    else:
        form = UserEditForm(
            initial ={
                'last_name': usuario.last_name,
                'first_name':usuario.first_name,
                'email': usuario.email,
                'password': usuario.password
            }
        )
    return render(request, "form_user.html",{"form": form})

@login_required
def form_articles(request):
    articles_list = Article.objects.all()
    return render(request, "form_articles.html", {"articles_list": articles_list})

@login_required
def form_experience(request):
    experience_list = Experience.objects.all()
    return render(request, "form_experience.html",{"experience_list": experience_list})

@login_required
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
        subname=request.POST['articles_subname']
        text=request.POST['articles_text']
        year=request.POST['articles_year']

        article =  Article.objects.create(articles_name=name,
                                          articles_text=text,
                                          articles_subname=subname,
                                          articles_year = year
                                          )
        return render(request, "success.html")
    else: return render(request, "error.html")

@login_required
def add_experience(request):
    if request.method == 'POST':
        name=request.POST['experience_name']
        institution=request.POST['experience_institution']

        article =  Experience.objects.create(experience_name=name,
                                             experience_institution=institution)
        return redirect('/menu/form_experience/')
    else: return render(request, "error.html")

@login_required
def add_work(request):
    if request.method == 'POST':
        name=request.POST['work_name']
        url=request.POST['work_url']
        year=request.POST['work_year']

        item =  Work.objects.create(work_name=name,
                                       work_url=url,
                                       work_year = year)
        return render(request, "success.html")
    else: return render(request, "error.html")

@login_required
def edit_experience(request, id):
    experience_list = Experience.objects.filter(id=id)
    return render(request, "edit_experience.html",{"experience_list": experience_list})

@login_required
def edit_article(request, id):
    article_list = Article.objects.filter(id=id)
    return render(request, "edit_article.html",{"article_list": article_list})

@login_required
def edit_work(request, id):
    work_list = Work.objects.filter(id=id)
    return render(request, "edit_work.html",{"work_list": work_list})

@login_required
def delete_experience(request, id):
    item = Experience.objects.get(id=id)
    item.delete()
    return redirect('/menu/form_experience/')

@login_required
def delete_article(request, id):
    item = Article.objects.get(id=id)
    item.delete()
    return redirect('/menu/form_articles/')

@login_required
def delete_work(request, id):
    item = Work.objects.get(id=id)
    item.delete()
    return redirect('/menu/form_my_work/')

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

@login_required
def update_article(request):
        article_id=request.POST['article_id']
        name=request.POST['article_name']
        text=request.POST['article_text']

        article =  Article.objects.get(id=article_id)
        article.articles_name = name
        article.articles_text = text
        article.save()

        messages.success(request, 'Articulo actualizada')

        return redirect('/menu/form_articles/')

@login_required
def update_work(request):
        work_id=request.POST['work_id']
        name=request.POST['work_name']
        url=request.POST['work_url']
        year=request.POST['work_year']

        work =  Work.objects.get(id=work_id)
        work.work_name = name
        work.work_url = url
        work.work_year = year
        work.save()

        messages.success(request, 'Trabajo actualizado')

        return redirect('/menu/form_my_work/')

def end_session (request):
    logout(request)
    return redirect('/')