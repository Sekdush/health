# Generated by Django 2.1 on 2020-01-30 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dicEntry', '0003_entry_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entrys', to='category.Category', verbose_name='分类id外键'),
        ),
    ]