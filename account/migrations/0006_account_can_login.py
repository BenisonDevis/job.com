# Generated by Django 4.2 on 2023-04-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_account_active_alter_account_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="can_login",
            field=models.BooleanField(default=True),
        ),
    ]
