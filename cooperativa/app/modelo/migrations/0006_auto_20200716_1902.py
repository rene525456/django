# Generated by Django 3.0.7 on 2020-07-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0005_auto_20200716_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
