# Generated by Django 2.2.2 on 2020-04-08 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200408_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='expire_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_value',
            field=models.CharField(max_length=1000),
        ),
    ]
