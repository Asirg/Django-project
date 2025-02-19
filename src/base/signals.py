from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Technology
from users.models import SkillLevel


@receiver(post_save, sender=Technology)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        for i in range(1, 11):
            SkillLevel.objects.create(
                technology = instance,
                score = i
            )