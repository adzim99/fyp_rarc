# Generated by Django 4.0.1 on 2022-01-25 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_rename_feedback_officefeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='profile_pic',
        ),
    ]