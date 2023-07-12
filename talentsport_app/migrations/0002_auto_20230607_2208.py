# Generated by Django 3.2.12 on 2023-06-07 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talentsport_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date mise à jour'),
        ),
        migrations.AlterField(
            model_name='postcategeory',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='postcategeory',
            name='designation',
            field=models.CharField(max_length=30, verbose_name='Désignation'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talentsport_app.postcategeory', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='discipline_sportive',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='talentsport_app.disciplinesportive', verbose_name='Discipline Sportive'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Photos'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_valid',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Valide'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=models.TextField(verbose_name='Texte'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='videos',
            field=models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d', verbose_name='Vidéos'),
        ),
    ]
