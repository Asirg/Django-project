from django.contrib import admin
from . import models


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name']