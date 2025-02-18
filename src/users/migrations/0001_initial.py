# Generated by Django 5.1.6 on 2025-02-18 09:12

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.technology')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('descripion', models.TextField(blank=True, null=True)),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumers', to='base.domain')),
                ('primary_specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_consumers', to='base.specialization')),
                ('secondary_specializations', models.ManyToManyField(related_name='secondary_consumers', to='base.specialization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(related_name='users', to='users.userskill')),
            ],
        ),
    ]
