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
from django.contrib import admin
from django.urls import include, path
from core import views
from django.conf.urls import handler404

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('about/', views.presentation, name="Index"),
    path('', views.presentation, name="Index"),
    path('my_work/', views.my_work, name="MyWork"),
    path('articles/', views.articles, name="Articles"),
    path('menu/article/<id>', views.article, name="ArticleSearch"),
    path('experience/', views.experience, name="Experience"),
    path('menu/', views.menu, name="Menu"),
    path('menu/form_articles/', views.form_articles, name="FormArticles"),
    path('menu/form_experience/', views.form_experience, name="FormExperience"),
    path('menu/form_my_work/', views.form_my_work, name="FormMyWork"),
    path('menu/add_article/', views.add_article, name="AddArticle"),
    path('menu/add_experience/', views.add_experience, name="AddExperience"),
    path('menu/add_work/', views.add_work, name="AddWork"),
    path('menu/edit_user/', views.edit_user, name="EditUser"),
    path('menu/edit_experience/<id>', views.edit_experience, name="EditExperience"),
    path('menu/edit_article/<id>', views.edit_article, name="EditArticle"),
    path('menu/edit_work/<id>', views.edit_work, name="EditWork"),
    path('menu/delete_experience/<id>', views.delete_experience, name="DeleteExperience"),
    path('menu/delete_article/<id>', views.delete_article, name="DeleteArticle"),
    path('menu/delete_work/<id>', views.delete_work, name="DeleteWork"),
path('menu/update_user/', views.update_user, name="UpdateUser"),
    path('menu/update_experience/', views.update_experience, name="UpdateExperience"),
    path('menu/update_article/', views.update_article, name="UpdateArticle"),
    path('menu/update_work/', views.update_work, name="UpdateWork"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('end/' , views.end_session, name="EndSession")
]
handler404 = 'core.views.error'