# Generated by Django 4.2.2 on 2023-06-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image_name",
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(null=True, upload_to="posts"),
        ),
    ]
