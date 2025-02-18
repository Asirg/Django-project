from django.contrib import admin
from . import models


@admin.register(models.UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    ...

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ...