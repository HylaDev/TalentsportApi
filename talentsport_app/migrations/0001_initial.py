# Generated by Django 4.1.7 on 2023-03-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nom')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Téléphone')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='Ville')),
                ('date_of_born', models.DateField(verbose_name='Date de naissance')),
                ('adress', models.TextField(verbose_name='Adresse')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('is_actif', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]