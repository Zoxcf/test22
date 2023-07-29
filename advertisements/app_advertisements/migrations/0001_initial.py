# Generated by Django 4.2.3 on 2023-07-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='название')),
                ('descriptions', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='цена')),
                ('trades', models.BooleanField(help_text='Если хотим торговаться', verbose_name='торг')),
                ('date_now', models.DateField(auto_now_add=True, verbose_name='Создание дата')),
                ('date_update', models.DateField(auto_now=True, verbose_name='Обновление дата')),
            ],
        ),
    ]
