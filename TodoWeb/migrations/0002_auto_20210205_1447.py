# Generated by Django 3.1.4 on 2021-02-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abcd',
            name='status',
            field=models.CharField(max_length=4),
        ),
    ]
