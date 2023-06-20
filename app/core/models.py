from django.db import models

class Work(models.Model):
    work_name = models.CharField(max_length=50)
    work_url = models.CharField(max_length=150)

    def __str__(self):
        return f"Work: {self.work_name}"

    
class Article(models.Model):
    articles_name = models.CharField(max_length=50)
    articles_text = models.TextField()

    def __str__(self):
        return f"Article: {self.articles_name}"

class Experience(models.Model):
    experience_name = models.CharField(max_length=50)
    experience_institution = models.CharField(max_length=50)

    def __str__(self):
        return f"Experience: {self.experience_name}"