# Generated by Django 2.2.5 on 2020-01-13 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfb', '0017_teamseasonstat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamseason',
            name='loss',
        ),
        migrations.RemoveField(
            model_name='teamseason',
            name='win',
        ),
    ]
