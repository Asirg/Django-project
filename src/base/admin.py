from django.contrib import admin
from . import models


@admin.register(models.Technology)
class TechnologyAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Industry)
class IndustryAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    ...