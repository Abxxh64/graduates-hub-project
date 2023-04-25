# Generated by Django 4.2 on 2023-04-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Pos', 'Post'), ('Pro', 'Project'), ('Job', 'Job')], max_length=3),
        ),
        migrations.AlterField(
            model_name='skill',
            name='field',
            field=models.CharField(choices=[('Embedded Systesm', 'Embedded Systems'), ('App Development', 'App Development'), ('Programming Language', 'Programming Language'), ('Graphic Design', 'Graphics Design'), ('Machine Learning', 'Machine Learning'), ('Databases', 'Databases'), ('Web Backend', 'Web Backend'), ('Web Frontend', 'Web Frontend')], max_length=40),
        ),
    ]