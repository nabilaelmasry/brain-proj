# Generated by Django 4.0.6 on 2022-07-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_alter_results_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
