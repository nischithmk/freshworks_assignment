# Generated by Django 3.1.4 on 2020-12-31 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table1',
            name='age',
        ),
    ]
