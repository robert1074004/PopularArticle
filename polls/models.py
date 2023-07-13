from django.db import models
from django.utils import timezone
from faker import Faker

fake = Faker()
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField(default = fake.paragraph)
    pub_date = models.DateTimeField(default=timezone.now)

class User(models.Model):
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=200)