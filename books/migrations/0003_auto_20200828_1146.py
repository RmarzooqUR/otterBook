# Generated by Django 3.0.8 on 2020-08-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200828_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='asset',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
