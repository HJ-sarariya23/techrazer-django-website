# Generated by Django 3.1.7 on 2021-03-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
