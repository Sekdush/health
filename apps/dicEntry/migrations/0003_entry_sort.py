# Generated by Django 2.1 on 2020-01-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicEntry', '0002_auto_20200125_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='sort',
            field=models.IntegerField(blank=True, default=999, null=True, verbose_name='条目排序'),
        ),
    ]
