# Generated by Django 3.1.4 on 2020-12-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0004_admins_number_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientId', models.CharField(blank=True, max_length=22, null=True)),
                ('adminId', models.CharField(blank=True, max_length=22, null=True)),
            ],
        ),
    ]
