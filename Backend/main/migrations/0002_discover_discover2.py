# Generated by Django 4.2.2 on 2023-07-03 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='discover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='addimg/')),
            ],
        ),
        migrations.CreateModel(
            name='discover2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('cover2', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='addimg/')),
            ],
        ),
    ]
