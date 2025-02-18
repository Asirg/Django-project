from django.contrib import admin
from . import models


@admin.register(models.LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    list_display = [
        'language__name', 'level'
    ]

@admin.register(models.SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = [
        'technology__name', 'score'
    ]
@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Vacansy)
class VacansyAdmin(admin.ModelAdmin):
    list_display = [
        'header', 
    ]

    fieldsets = [
        (
            None,
            {"fields":[
                ('header', 'specialization'),
            ]}
        ),
        (
            "Language",
            {"fields":[
                ('primary_language', 'secondary_language'),
            ]}
        ),
        (
            "Technologies",
            {"fields":[
                ('technologies'),
            ]}
        )
    ]