# Generated by Django 2.0.9 on 2018-10-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/img/default.png', height_field='url_height', upload_to='img/', width_field='url_width'),
        ),
    ]