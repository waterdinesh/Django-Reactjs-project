# Generated by Django 4.2.2 on 2023-07-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_discover2_cover2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailAddress', models.CharField(max_length=20)),
                ('Employee', models.CharField(max_length=500)),
                ('YourName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('LocalTime', models.CharField(max_length=50)),
                ('Payment', models.IntegerField()),
                ('PhoneNumber', models.IntegerField()),
                ('Service', models.CharField(max_length=50)),
            ],
        ),
    ]
