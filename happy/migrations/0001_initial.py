# Generated by Django 3.2.6 on 2021-08-23 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('detail', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('picture', models.CharField(max_length=128)),
                ('category', models.CharField(choices=[('Tincturas', 'tincturas'), ('Cremas', 'cremas'), ('Body Lotion', 'body_lotion'), ('Gomitas', 'gomitas'), ('Vapes', 'vapes')], max_length=20)),
            ],
        ),
    ]
