# Generated by Django 4.2.11 on 2024-04-16 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['id'], 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
    ]
