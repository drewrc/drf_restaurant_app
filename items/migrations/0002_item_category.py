# Generated by Django 4.1.7 on 2023-02-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='category', max_length=30),
        ),
    ]
