# Generated by Django 4.1.3 on 2022-12-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_result_totalquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='toalMarks',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='totalQuestions',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]