# Generated by Django 4.2 on 2023-04-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0003_addproject"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skill", models.CharField(max_length=50)),
                ("percentage", models.IntegerField()),
            ],
        ),
    ]
