# Generated by Django 5.0.2 on 2024-04-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_alter_snitch_snitchtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snitch',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='messages', to='projectApp.message'),
        ),
    ]
