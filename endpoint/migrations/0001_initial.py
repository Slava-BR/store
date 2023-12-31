# Generated by Django 5.0 on 2023-12-20 10:53

import endpoint.Validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('main', models.BooleanField()),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('sale', models.PositiveSmallIntegerField(validators=[endpoint.Validators.percent_is_valid])),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d/')),
                ('size', models.JSONField(default={'size': []})),
                ('type', models.CharField(choices=[('Hoodie', 'Худи'), ('Sweatshirts', 'Свитшоты'), ('T-shirts', 'Футболки'), ('Longsleeve', 'Лонгсливы')], max_length=30)),
                ('collections', models.CharField(choices=[('VSRAP', 'VSRAP'), ('CMH', 'CMH')], max_length=30)),
                ('textile', models.CharField(choices=[('Cooler', 'кулирка')], max_length=30)),
                ('material', models.CharField(choices=[('Cotton', 'Хлопок')], max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('slug_title', models.SlugField(max_length=100, unique=True, verbose_name='URL_TITLE')),
                ('slug_collection', models.SlugField(max_length=100, unique=True, verbose_name='URL_COLLECTION')),
            ],
        ),
    ]
