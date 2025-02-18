from django.contrib import admin
from . import models


@admin.register(models.UserLanguage)
class UserLanguageAdmin(admin.ModelAdmin):
    list_display = [
        'language__name', 'level'
    ]

@admin.register(models.UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = [
        'technology__name', 'score'
    ]

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user__username', 
        'city',
        'country',
        'id', 
    ]

    fieldsets = [
        (
            None,
            {"fields":[
                ('user', 'avatar'),
            ]}
        ),
        (
            "About User",
            {"fields":[
                ('city', 'country'),
                'description'
            ]}
        ),
        (
            "Profession",
            {"fields":[
                ('domain', 'primary_specialization'),
                ('secondary_specializations', 'skills', 'languages')
            ]}
        )
    ]