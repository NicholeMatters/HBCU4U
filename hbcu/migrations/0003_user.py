# Generated by Django 3.0.8 on 2020-07-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbcu', '0002_college_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.TextField(blank=True, null=True)),
            ],
            options={
                'order_with_respect_to': 'lastname',
            },
        ),
    ]
