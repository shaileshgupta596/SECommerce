# Generated by Django 5.0.1 on 2024-01-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('all', 'All'), ('news', 'News'), ('food', 'Food'), ('travel', 'Travel')], default='All', max_length=50, null=True),
        ),
    ]
