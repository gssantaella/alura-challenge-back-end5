# Generated by Django 3.2.5 on 2022-11-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflixbe', '0002_auto_20221029_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=7)),
            ],
        ),
    ]
