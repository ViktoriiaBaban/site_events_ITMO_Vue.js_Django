# Generated by Django 4.1.5 on 2023-01-13 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_alter_event_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="date",
            field=models.DateTimeField(default="2022-10-16 12:00"),
            preserve_default=False,
        ),
    ]
