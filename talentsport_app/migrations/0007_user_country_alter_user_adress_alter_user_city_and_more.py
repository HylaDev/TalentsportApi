# Generated by Django 4.2.3 on 2023-09-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talentsport_app', '0006_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='adress',
            field=models.TextField(blank=True, null=True, verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ville'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_born',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_actif',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(blank=True, choices=[('DEBUTANT', 'Débutant'), ('INTERMEDIAIRE', 'Intermédiaire'), ('PASSIONNER', 'Passioner'), ('PROFESSIONNEL', 'Professionnel')], max_length=15, null=True, verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Téléphone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='strong_foot',
            field=models.CharField(blank=True, choices=[('GAUCHE', 'Gauche'), ('DROIT', 'Droit')], max_length=15, null=True, verbose_name='Pied Fort'),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Poids'),
        ),
    ]
