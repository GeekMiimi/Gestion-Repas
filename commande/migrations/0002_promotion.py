# Generated by Django 4.2.1 on 2023-07-05 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('reduction', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
