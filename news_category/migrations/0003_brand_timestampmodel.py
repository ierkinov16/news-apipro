# Generated by Django 4.2.1 on 2023-05-17 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_category', '0002_category_image_category_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='brand')),
            ],
        ),
        migrations.CreateModel(
            name='TimestampModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
