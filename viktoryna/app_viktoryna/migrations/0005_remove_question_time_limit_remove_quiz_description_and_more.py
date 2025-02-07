# Generated by Django 5.1.4 on 2025-02-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_viktoryna', '0004_remove_answer_answer_text_remove_question_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time_limit',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='description',
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Правильна відповідь'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Текст відповіді'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Текст питання'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Назва вікторини'),
        ),
    ]
