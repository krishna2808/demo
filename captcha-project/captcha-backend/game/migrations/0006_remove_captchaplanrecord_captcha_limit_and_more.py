# Generated by Django 5.0.1 on 2024-01-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captchaplanrecord',
            name='captcha_limit',
        ),
        migrations.AddField(
            model_name='captchaplanrecord',
            name='is_plan_active',
            field=models.BooleanField(default=False),
        ),
    ]
