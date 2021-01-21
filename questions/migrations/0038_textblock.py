# Generated by Django 3.0.1 on 2021-01-21 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0037_auto_20210118_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('name_is', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_de', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('description_is', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_de', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('expire', models.DateTimeField(blank=True, null=True)),
                ('slot', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('Texti',),
                'verbose_name_plural': 'Textar',
            },
        ),
    ]
