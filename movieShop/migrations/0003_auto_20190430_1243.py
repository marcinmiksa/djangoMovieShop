# Generated by Django 2.2 on 2019-04-30 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieShop', '0002_auto_20190430_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
