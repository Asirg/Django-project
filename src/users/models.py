from django.db import models
from django.contrib.auth.models import User

from base.models import Specialization, Domain, Technology, Language, LanguageLevel, SkillLevel


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)

    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    primary_specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name="primary_consumers")
    secondary_specializations = models.ManyToManyField(Specialization, related_name="secondary_consumers", blank=True )

    languages = models.ManyToManyField(LanguageLevel, related_name="speakers", blank=True)
    skills = models.ManyToManyField(SkillLevel, related_name="users", blank=True)

    def __str__(self):
        return self.user.username