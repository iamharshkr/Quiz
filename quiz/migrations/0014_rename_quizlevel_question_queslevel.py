# Generated by Django 4.1.3 on 2022-12-06 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_question_placeholder_alter_question_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quizLevel',
            new_name='quesLevel',
        ),
    ]