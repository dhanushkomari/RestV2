# Generated by Django 3.1.4 on 2022-02-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0007_auto_20220127_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocation',
            name='status',
            field=models.CharField(choices=[('incomplete', 'incomplete'), ('pending', 'pending'), ('complete', 'completed')], default='incomplete', max_length=20),
        ),
    ]
