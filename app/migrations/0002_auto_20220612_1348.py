# Generated by Django 3.1.3 on 2022-06-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
