# Generated by Django 3.2.6 on 2021-08-23 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]