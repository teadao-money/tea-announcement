# Generated by Django 4.2.10 on 2024-03-26 03:03

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]
