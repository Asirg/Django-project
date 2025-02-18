from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()
    
    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    technilogies = models.ManyToManyField(
        Technology,
        related_name="specializations",
    )

    def __str__(self):
        return self.name