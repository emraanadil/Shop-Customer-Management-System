# Generated by Django 3.1.7 on 2021-09-14 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0005_auto_20210914_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=10),
            preserve_default=False,
        ),
    ]
