# Generated by Django 3.0.4 on 2020-04-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0009_auto_20200402_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakfastmenu',
            name='front_thumb_img_url',
            field=models.ImageField(default='Upload image', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='lunchmenu',
            name='front_thumb_img_url',
            field=models.ImageField(default='Upload image', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='soupmenu',
            name='front_thumb_img_url',
            field=models.ImageField(default='Upload image', upload_to='images/'),
        ),
    ]
