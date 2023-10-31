# Generated by Django 3.2 on 2023-10-09 15:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='年齢')),
                ('gender', models.IntegerField(choices=[(1, '男性'), (2, '女性'), (3, 'その他')], default=1, verbose_name='性別')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス入力')),
                ('phone_number', models.CharField(max_length=12, verbose_name='電話番号')),
            ],
        ),
    ]
