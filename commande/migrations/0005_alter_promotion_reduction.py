# Generated by Django 4.2.1 on 2023-07-06 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0004_alter_promotion_reduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='reduction',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
