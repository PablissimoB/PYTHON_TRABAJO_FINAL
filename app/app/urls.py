"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('about/', views.presentation, name="Index"),
    path('', views.presentation, name="Index"),
    path('my_work/', views.my_work, name="MyWork"),
    path('articles/', views.articles, name="Articles"),
    path('experience/', views.experience, name="Experience"),
    path('menu/', views.menu, name="Menu"),
    path('menu/form_articles/', views.form_articles, name="FormArticles"),
    path('menu/form_experience/', views.form_experience, name="FormExperience"),
    path('menu/form_my_work/', views.form_my_work, name="FormMyWork"),
    path('menu/add_article/', views.add_article, name="AddArticle"),
    path('menu/add_experience/', views.add_experience, name="AddExperience"),
    path('menu/add_work/', views.add_work, name="AddWork"),
    path('menu/edit_experience/<id>', views.edit_experience, name="EditExperience"),
    path('menu/update_experience/', views.update_experience, name="UpdateExperience"),
]
