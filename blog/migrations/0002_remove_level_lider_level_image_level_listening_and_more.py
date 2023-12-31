# Generated by Django 4.2.5 on 2023-09-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='lider',
        ),
        migrations.AddField(
            model_name='level',
            name='image',
            field=models.ImageField(default=1, upload_to='level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='listening',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='reading',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='speaking',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='writing',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
