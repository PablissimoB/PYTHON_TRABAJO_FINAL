from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='images', null=True, blank = True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    @property
    def d(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Work(models.Model):
    work_name = models.CharField(max_length=50)
    work_url = models.CharField(max_length=150)
    work_year = models.IntegerField(max_length=4)

    def __str__(self):
        return f"Work: {self.work_name}"

class Article(models.Model):
    articles_name = models.CharField(max_length=80)
    articles_subname = models.CharField(max_length=100)
    articles_text = models.TextField()
    articles_year = models.IntegerField(max_length=4)

    def __str__(self):
        return f"Article: {self.articles_name}"

class Experience(models.Model):
    experience_name = models.CharField(max_length=50)
    experience_institution = models.CharField(max_length=50)

    def __str__(self):
        return f"Experience: {self.experience_name}"