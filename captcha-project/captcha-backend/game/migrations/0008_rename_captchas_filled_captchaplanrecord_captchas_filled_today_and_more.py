# Generated by Django 5.0.1 on 2024-01-31 17:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_captchaplanrecord_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='captchaplanrecord',
            old_name='captchas_filled',
            new_name='captchas_filled_today',
        ),
        migrations.AddField(
            model_name='captchaplanrecord',
            name='last_captcha_fill_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='captchaplanrecord',
            name='total_captchas_filled',
            field=models.PositiveIntegerField(default=0),
        ),
    ]