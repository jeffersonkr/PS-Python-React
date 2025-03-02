# Generated by Django 4.1.6 on 2023-02-12 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("market", "0005_add_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
