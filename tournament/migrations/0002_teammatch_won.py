# Generated by Django 5.0 on 2023-12-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammatch',
            name='won',
            field=models.BooleanField(default=False),
        ),
    ]
