# Generated by Django 3.0.8 on 2020-08-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20200828_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='asset',
            field=models.FileField(upload_to=''),
        ),
    ]