# Generated by Django 3.0.1 on 2020-11-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20200604_2119'),
        ('questions', '0017_auto_20201119_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': ('Próf/æfing',), 'verbose_name_plural': 'Próf/æfing'},
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='omit_known',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='question_questionnaire_owner', related_query_name='questionnaire', to='person.PersonUser'),
        ),
    ]
