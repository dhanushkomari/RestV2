# Generated by Django 3.1.4 on 2022-02-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0009_chef_chef_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='status',
            field=models.CharField(choices=[('incomplete', 'incomplete'), ('pending', 'pending'), ('complete', 'complete')], default='incomplete', max_length=20),
        ),
    ]