# Generated by Django 3.2.16 on 2023-02-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shahar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('img', models.ImageField(default='', upload_to='')),
            ],
            options={
                'verbose_name': 'shaxar',
                'verbose_name_plural': 'shaxarlar',
            },
        ),
    ]