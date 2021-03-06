# Generated by Django 2.1 on 2020-01-24 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='条目标题')),
                ('remark', models.CharField(blank=True, max_length=255, null=True, verbose_name='条目内容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category', verbose_name='分类id外键')),
            ],
            options={
                'verbose_name': '条目信息表',
                'verbose_name_plural': '条目信息表',
                'db_table': 'h_entry',
            },
        ),
        migrations.CreateModel(
            name='Entryship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_id', models.IntegerField(blank=True, null=True, verbose_name='条目关联分类id外键')),
                ('from_entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_entry', to='dicEntry.Entry', verbose_name='条目id外键')),
                ('to_entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_entry', to='dicEntry.Entry', verbose_name='条目关联id外键')),
            ],
            options={
                'verbose_name': '条目信息自关联表',
                'verbose_name_plural': '条目信息自关联表',
                'db_table': 'h_entry_ship',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='entrys',
            field=models.ManyToManyField(through='dicEntry.Entryship', to='dicEntry.Entry'),
        ),
    ]
