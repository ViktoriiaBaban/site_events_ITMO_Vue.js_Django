# Generated by Django 4.1.5 on 2023-01-14 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_event_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="category",
        ),
        migrations.RemoveField(
            model_name="event",
            name="district",
        ),
        migrations.RemoveField(
            model_name="event",
            name="type_event",
        ),
    ]
