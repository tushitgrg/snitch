# Generated by Django 5.0.2 on 2024-04-11 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0005_snitch_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snitch',
            name='replies',
        ),
        migrations.AlterField(
            model_name='snitch',
            name='Title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replytext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectApp.message')),
                ('snitchm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectApp.snitch')),
            ],
        ),
    ]
