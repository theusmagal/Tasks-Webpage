# Generated by Django 5.0.3 on 2024-03-19 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_task_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
