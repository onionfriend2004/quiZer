# Generated by Django 5.0.6 on 2024-06-27 08:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='User_quizes',
            new_name='User_quiz',
        ),
    ]