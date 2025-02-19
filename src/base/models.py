from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Language(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    def __str__(self):
        return self.name
    
class LanguageLevel(models.Model):
    LEVEL_OF_LANGUAGE_PROFICIENCY = [
        ("A1", "Beginner"),
        ("A2", "Elementary"),
        ("B1", "Intermediate"),
        ("B2", "Upper Intermediate"),
        ("C1", "Advanced"),
        ("C2", "Proficiency")
    ]
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    level = models.CharField(
        max_length=50,
        choices=LEVEL_OF_LANGUAGE_PROFICIENCY,
    )

    def __str__(self):
        return f"{self.language.name}:{self.level}"

class Technology(models.Model):
    name = models.CharField(max_length=150)
    desctiption = models.TextField()

    def __str__(self):
        return self.name

class SkillLevel(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    score = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return f"{self.technology.name}:{self.score}"

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
    

class Vacansy(models.Model):
    header = models.CharField(max_length=150)

    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

    primary_language = models.ForeignKey(LanguageLevel, on_delete=models.SET_NULL, null=True, related_name="primary_vacansies")
    secondary_language = models.ManyToManyField(LanguageLevel, related_name="secondary_vacansies")
    technologies = models.ManyToManyField(Technology, related_name="vacansies")

    def __str__(self):
        return self.header