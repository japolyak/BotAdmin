# Generated by Django 4.1.1 on 2022-09-26 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_clients_client_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartmeta',
            old_name='descrition',
            new_name='descrpition',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='descrition',
            new_name='descrpition',
        ),
    ]
