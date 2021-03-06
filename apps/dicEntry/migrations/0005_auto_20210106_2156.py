# Generated by Django 3.0.8 on 2021-01-06 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('dicEntry', '0004_auto_20200130_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['sort', 'id'], 'verbose_name': '条目信息表', 'verbose_name_plural': '条目信息表'},
        ),
        migrations.AlterModelOptions(
            name='entryship',
            options={'ordering': ['from_entry'], 'verbose_name': '条目信息自关联表', 'verbose_name_plural': '条目信息自关联表'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entrys', to='category.Category', verbose_name='分类id外键'),
        ),
        migrations.AlterField(
            model_name='entryship',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.Category', verbose_name='条目关联分类id外键'),
        ),
    ]
