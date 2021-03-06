# Generated by Django 2.2.2 on 2020-04-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200408_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=16, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('username', models.CharField(max_length=16, verbose_name='用户名')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='余额')),
                ('gender', models.PositiveSmallIntegerField(default=0, verbose_name='性别')),
                ('tel', models.CharField(default='', max_length=11, verbose_name='电话')),
            ],
        ),
        migrations.DeleteModel(
            name='Session',
        ),
    ]
