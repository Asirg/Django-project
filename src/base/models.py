from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

class Industry(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

class Domain(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

class Specialization(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    technilogies = models.ManyToManyField(
        Technology,
        related_name="specializations",
    )