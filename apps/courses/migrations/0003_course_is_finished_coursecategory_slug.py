# Generated by Django 4.1.7 on 2023-03-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_author_alter_course_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Kurs tugadimi'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
