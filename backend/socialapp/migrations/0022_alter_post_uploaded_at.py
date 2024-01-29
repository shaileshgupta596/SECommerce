# Generated by Django 5.0.1 on 2024-01-29 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0021_alter_post_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
