# Generated by Django 4.2 on 2023-04-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0004_alter_account_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]
