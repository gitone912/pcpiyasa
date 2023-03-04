# Generated by Django 4.1.6 on 2023-03-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphics_cards', '0002_ok_delete_graphicscard'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicsCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('graphic_card_name', models.CharField(max_length=200)),
                ('graphic_card_brand', models.CharField(max_length=200)),
                ('graphic_card_model', models.CharField(max_length=200)),
                ('graphic_card_memory', models.CharField(max_length=200)),
                ('graphic_card_memory_interface', models.CharField(max_length=200)),
                ('graphic_card_length', models.CharField(max_length=200)),
                ('graphic_card_interface', models.CharField(max_length=200)),
                ('graphic_card_chipset', models.CharField(max_length=200)),
                ('graphic_card_base_clock', models.CharField(max_length=200)),
                ('graphic_card_clock_speed', models.CharField(max_length=200)),
                ('graphic_card_frame_sync', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('graphic_card_image_url', models.URLField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='ok',
        ),
    ]