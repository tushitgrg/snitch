# Generated by Django 5.0.2 on 2024-04-10 17:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0004_alter_snitch_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='snitch',
            name='Title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
