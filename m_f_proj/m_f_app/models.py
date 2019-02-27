from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField()
    text = models.CharField()
    created_date = models.DateField()
    published_date = models.DateField()

