# Generated by Django 4.2 on 2023-04-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0009_alter_account_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]