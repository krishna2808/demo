# Generated by Django 5.0.1 on 2024-02-06 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_id',
            field=models.CharField(default='7c0c247', editable=False, max_length=7),
        ),
    ]
