# Generated by Django 3.0.4 on 2020-03-30 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_soupmenu_soup_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='soupmenu',
            name='soup_description',
            field=models.TextField(default='Describe soup here'),
        ),
    ]
