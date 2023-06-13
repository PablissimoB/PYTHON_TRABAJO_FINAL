from django.db import models

class Work(models.Model):
    work_name = models.CharField(max_length=50)
    work_url = models.CharField(max_length=50)

    def __str__(self):
        return f"Work: {self.work_name}"
    
    def __init__(self, work_name, work_url):
        self.work_name = work_name
        self.work_url = work_url

    
class Article(models.Model):
    articles_name = models.CharField(max_length=50)
    articles_text = models.TextField()

    def __str__(self):
        return f"Article: {self.articles_name}"

    def __init__(self, articles_name, articles_text):
            self.articles_name = articles_name
            self.articles_text = articles_text

class Experience(models.Model):
    experience_name = models.CharField(max_length=50)
    experience_institution = models.CharField(max_length=50)

    def __str__(self):
        return f"Experience: {self.experience_name}"
    
    def __init__(self, experience_name, experience_institution):
            self.experience_name = experience_name
            self.experience_institution = experience_institution