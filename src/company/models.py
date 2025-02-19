from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150)
    url = models.SlugField()
    link = models.SlugField()

# Можно организоваться свою компанию, разные настройки и тд