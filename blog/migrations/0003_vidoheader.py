# Generated by Django 4.2.2 on 2023-09-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_level_lider_level_image_level_listening_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vidoheader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidio', models.FileField(upload_to='')),
            ],
        ),
    ]
