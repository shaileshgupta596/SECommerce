# Generated by Django 5.0.1 on 2024-01-29 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0020_alter_post_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 29, 17, 16, 22, 391112, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
