# Generated by Django 3.1.5 on 2021-01-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210113_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='upload'),
        ),
    ]
