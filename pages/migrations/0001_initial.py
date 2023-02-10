# Generated by Django 4.1.5 on 2023-02-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(height_field=340, upload_to='', width_field=720)),
                ('comments', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]