# Generated by Django 4.0 on 2021-12-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('code', models.CharField(max_length=8, verbose_name='Код ссылки')),
            ],
        ),
    ]
