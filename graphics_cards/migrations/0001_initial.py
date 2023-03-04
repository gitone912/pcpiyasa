# Generated by Django 4.1.6 on 2023-03-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicsCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('memory', models.CharField(max_length=200)),
                ('memory_interface', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=200)),
                ('interface', models.CharField(max_length=200)),
                ('chipset', models.CharField(max_length=200)),
                ('base_clock', models.CharField(max_length=200)),
                ('clock_speed', models.CharField(max_length=200)),
                ('frame_sync', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_url', models.URLField(max_length=500)),
            ],
        ),
    ]