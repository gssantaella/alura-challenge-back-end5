# Generated by Django 3.2.5 on 2022-10-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflixbe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='descricao',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.URLField(max_length=50),
        ),
    ]
