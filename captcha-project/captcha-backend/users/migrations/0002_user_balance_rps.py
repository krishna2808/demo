# Generated by Django 5.0.1 on 2024-01-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance_rps',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
