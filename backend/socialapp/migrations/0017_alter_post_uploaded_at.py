# Generated by Django 5.0.1 on 2024-01-28 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0016_alter_post_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 28, 8, 53, 24, 369080, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]