# Generated by Django 4.0.6 on 2022-08-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=38)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=38)),
                ('apellido', models.CharField(max_length=38)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=38)),
                ('apellido', models.CharField(max_length=38)),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=38)),
            ],
        ),
    ]
