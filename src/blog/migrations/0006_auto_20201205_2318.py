# Generated by Django 3.0.1 on 2020-12-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201205_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default='yes'),
        ),
    ]
