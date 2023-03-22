# Generated by Django 4.1.5 on 2023-01-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_event_category_event_district_event_type_event"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="contact_name",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="event",
            name="contact_number",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(
                choices=[
                    ("Спорт и фитнес", "Спорт и фитнес"),
                    ("Искусство и культура", "Искусство и культура"),
                    ("Природа", "Природа"),
                    ("Карьера и образование", "Карьера и образование"),
                    ("Театры", "Театры"),
                    ("Концерты", "Концерты"),
                ],
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="description",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]