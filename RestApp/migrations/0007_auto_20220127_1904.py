# Generated by Django 3.1.4 on 2022-01-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0006_auto_20220126_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
