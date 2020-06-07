# Generated by Django 3.0.5 on 2020-04-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhlogFeeder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phlog_title', models.CharField(blank=True, default='Provide image a title', max_length=150)),
                ('phlog_description', models.TextField(blank=True, default='Write brief description here...')),
                ('phlog_image_url', models.ImageField(default='Upload image', upload_to='images/')),
                ('position', models.CharField(default='provide position number', max_length=150)),
                ('phlog_status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=10)),
            ],
        ),
    ]