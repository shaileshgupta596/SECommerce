# Generated by Django 5.0.1 on 2024-02-10 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0032_alter_post_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
    ]
