# Generated by Django 2.0.3 on 2018-09-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='st',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]