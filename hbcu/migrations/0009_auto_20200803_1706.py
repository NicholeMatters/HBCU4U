# Generated by Django 3.0.8 on 2020-08-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbcu', '0008_auto_20200803_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='campus_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='logo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
