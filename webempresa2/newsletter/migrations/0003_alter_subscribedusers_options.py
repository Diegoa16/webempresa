# Generated by Django 4.1.3 on 2022-11-12 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_subscribedusers_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribedusers',
            options={'verbose_name': 'Usuario suscrito', 'verbose_name_plural': 'Usuarios suscritos'},
        ),
    ]
