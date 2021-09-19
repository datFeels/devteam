# Generated by Django 3.2.6 on 2021-09-19 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_rename_class_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='name',
        ),
        migrations.AddField(
            model_name='lecture',
            name='lname',
            field=models.CharField(blank=True, max_length=20, verbose_name='课名称'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='knowledge',
            field=models.TextField(blank=True, verbose_name='知识点'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='课程'),
        ),
    ]
