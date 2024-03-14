# Generated by Django 4.0.6 on 2024-03-09 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_app', '0007_delete_page_remove_member_outstanding_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
