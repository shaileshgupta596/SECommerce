# Generated by Django 5.0.1 on 2024-01-28 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0018_alter_post_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 28, 9, 1, 1, 573331, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
