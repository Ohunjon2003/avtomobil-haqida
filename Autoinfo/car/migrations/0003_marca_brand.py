# Generated by Django 5.0.3 on 2024-05-21 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.brand'),
        ),
    ]