# Generated by Django 4.1.12 on 2023-11-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_location_event_description_location_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('imagine', models.BinaryField()),
            ],
        ),
    ]
