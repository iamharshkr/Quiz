# Generated by Django 4.1.3 on 2022-12-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_rename_toalmarks_quiz_totalmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quizLevel',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]