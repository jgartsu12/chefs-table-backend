# Generated by Django 3.0.4 on 2020-04-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_foodmenus_food_thumb_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='soupmenu',
            name='food_thumb_img',
            field=models.ImageField(default='Upload image', upload_to=''),
        ),
    ]