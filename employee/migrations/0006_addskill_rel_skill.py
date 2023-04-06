# Generated by Django 4.2 on 2023-04-06 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_company"),
        ("employee", "0005_profileedit"),
    ]

    operations = [
        migrations.AddField(
            model_name="addskill",
            name="rel_skill",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.employee",
            ),
        ),
    ]