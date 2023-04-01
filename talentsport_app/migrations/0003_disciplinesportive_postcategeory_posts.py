# Generated by Django 4.1.7 on 2023-04-01 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talentsport_app', '0002_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineSportive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostCategeory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('is_valid', models.BooleanField(blank=True, default=False, null=True)),
                ('videos', models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentsport_app.postcategeory')),
                ('discipline_sportive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='talentsport_app.disciplinesportive')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]