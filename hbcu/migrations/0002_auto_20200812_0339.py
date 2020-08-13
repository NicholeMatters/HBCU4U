# Generated by Django 3.0.8 on 2020-08-12 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hbcu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=3000)),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hbcu.State'),
        ),
    ]
