# Generated by Django 5.0.2 on 2024-04-11 12:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0008_remove_snitch_topics_snitch_topics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterModelOptions(
            name='snitch',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='snitch',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snitch',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='downvotes',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AlterField(
            model_name='message',
            name='upvotes',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
