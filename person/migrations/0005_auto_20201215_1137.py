# Generated by Django 3.0.1 on 2020-12-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='period_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='period_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
