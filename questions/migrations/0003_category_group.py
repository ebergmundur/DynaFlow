# Generated by Django 3.0.1 on 2020-06-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        # ('questions', '0002_auto_20200605_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='group',
            field=models.ManyToManyField(to='questions.Group'),
        ),
    ]
