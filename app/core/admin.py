from django.contrib import admin
from .models import Article, Experience, Work, Profile

admin.site.register(Article)
admin.site.register(Experience)
admin.site.register(Work)
admin.site.register(Profile)