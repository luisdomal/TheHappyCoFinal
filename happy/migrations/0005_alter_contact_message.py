# Generated by Django 3.2.6 on 2021-08-31 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]