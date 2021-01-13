# Generated by Django 3.1.5 on 2021-01-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_bookcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Author'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-code'], 'verbose_name_plural': 'Book'},
        ),
        migrations.AlterModelOptions(
            name='bookcomment',
            options={'ordering': ['id'], 'verbose_name_plural': 'Book Comment'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AddField(
            model_name='book',
            name='level',
            field=models.CharField(blank=True, choices=[('B', 'Basic'), ('M', 'Medium'), ('A', 'Advance')], max_length=5, null=True),
        ),
    ]
