# Generated by Django 4.2.6 on 2023-11-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='groupmodel',
            table='user_group',
        ),
        migrations.AlterModelTable(
            name='usermodel',
            table='user',
        ),
    ]