# Generated by Django 4.2 on 2023-04-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_company"),
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="companyprofile",
            name="rel_comp",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.company",
            ),
        ),
    ]
