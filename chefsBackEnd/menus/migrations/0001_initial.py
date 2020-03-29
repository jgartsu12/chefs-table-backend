# Generated by Django 3.0.4 on 2020-03-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(choices=[('BREAKFAST MENU', 'BREAKFAST MENU'), ('LUNCH MENU', 'LUNCH MENU'), ('SOUP MENU', 'SOUP MENU')], default='SOUP MENU', max_length=150)),
            ],
        ),
    ]
