# Generated by Django 4.2.4 on 2023-08-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vitura", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="description",
            field=models.CharField(
                blank=True, default="No description", max_length=2000, null=True
            ),
        ),
    ]