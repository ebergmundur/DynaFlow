# Generated by Django 3.0.1 on 2020-11-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200605_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': ('flokkur',), 'verbose_name_plural': 'flokkar'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': ('hópur',), 'verbose_name_plural': 'hópar'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': ('svar',), 'verbose_name_plural': 'svör'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': ('spurning',), 'verbose_name_plural': 'spurningar'},
        ),
        migrations.AlterModelOptions(
            name='questiongrouprelation',
            options={'verbose_name': ('tengd spurnin',), 'verbose_name_plural': 'tengdar spurningar'},
        ),
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': ('spurningalisti',), 'verbose_name_plural': 'spurningalistar'},
        ),
        migrations.AlterModelOptions(
            name='questionnairegrouprelation',
            options={'verbose_name': ('tengdur hópur',), 'verbose_name_plural': 'tengdir hópar'},
        ),
        migrations.AddField(
            model_name='option',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='image',
            field=models.ImageField(blank=True, upload_to='optionImage'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questionImage'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
