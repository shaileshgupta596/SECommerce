# Generated by Django 5.0.1 on 2024-01-26 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0010_rename_post_type_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uploaded_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 26, 18, 48, 58, 209935, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
