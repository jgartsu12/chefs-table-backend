# Generated by Django 3.0.4 on 2020-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0008_auto_20200401_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakfastMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Breakfast Menu', max_length=150)),
                ('name', models.CharField(default='Add items here', max_length=120)),
                ('description', models.TextField(default='Add items here')),
                ('front_thumb_img_url', models.ImageField(default='Upload image', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='LunchMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Lunch Menu', max_length=150)),
                ('name', models.CharField(default='Add items here', max_length=120)),
                ('description', models.TextField(default='Add items here')),
                ('front_thumb_img_url', models.ImageField(default='Upload image', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='FoodMenus',
        ),
        migrations.RenameField(
            model_name='soupmenu',
            old_name='soup_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='soupmenu',
            old_name='soup_thumb_img',
            new_name='front_thumb_img_url',
        ),
        migrations.RenameField(
            model_name='soupmenu',
            old_name='soup_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='soupmenu',
            name='soup_prices',
        ),
        migrations.RemoveField(
            model_name='soupmenu',
            name='soup_sizes',
        ),
        migrations.AddField(
            model_name='soupmenu',
            name='title',
            field=models.CharField(default='Soup Menu', max_length=150),
        ),
    ]
