# Generated by Django 3.0.1 on 2021-03-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0042_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='textblock',
            name='icon_code',
            field=models.CharField(default='class', max_length=200),
        ),
    ]
