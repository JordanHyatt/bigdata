# Generated by Django 2.2.5 on 2020-01-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfb', '0019_auto_20200119_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='surface',
            field=models.CharField(default='grass', max_length=200),
            preserve_default=False,
        ),
    ]