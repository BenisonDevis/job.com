# Generated by Django 4.2 on 2023-04-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("employee", "0016_applyjob_selected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileedit",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profileedit",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("O", "Outher")],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profileedit",
            name="location",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="profileedit",
            name="mobile_no",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name="profileedit",
            name="profile_title",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="profileedit",
            name="working_sts",
            field=models.CharField(
                blank=True,
                choices=[("frsh", "I'm Fresher"), ("exp", "I'm Experienced")],
                max_length=50,
                null=True,
            ),
        ),
    ]
