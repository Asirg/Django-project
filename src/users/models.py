from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import Specialization, Domain, Technology


class UserSkill(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    score = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    

    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL, null=True, blank=True, related_name="consumers")

    primary_specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name="primary_consumers")
    secondary_specializations = models.ManyToManyField(Specialization, related_name="secondary_consumers")

    skills = models.ManyToManyField(UserSkill, related_name="users")

    def __str__(self):
        return self.user.username