# Generated by Django 4.0.6 on 2024-03-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='B_id',
            field=models.IntegerField(default=0),
        ),
    ]
