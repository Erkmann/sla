# Generated by Django 3.0.5 on 2020-04-29 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appinscricao', '0002_auto_20200429_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='dhup',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
