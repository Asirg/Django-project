from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import Specialization, Domain, Technology, Language


class UserLanguage(models.Model):
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

class UserSkill(models.Model):
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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    

    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True, blank=True, related_name="consumers")

    primary_specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name="primary_consumers")
    secondary_specializations = models.ManyToManyField(Specialization, related_name="secondary_consumers", blank=True )

    languages = models.ManyToManyField(UserLanguage, related_name="speakers", blank=True)
    skills = models.ManyToManyField(UserSkill, related_name="users", blank=True)

    def __str__(self):
        return self.user.username