# Generated by Django 3.1.4 on 2020-12-23 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0005_clientadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='status',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='admins',
            name='activity',
            field=models.ForeignKey(blank=True, default='Активен', null=True, on_delete=django.db.models.deletion.CASCADE, to='telebot.activities', to_field='status'),
        ),
        migrations.AlterField(
            model_name='admins',
            name='name',
            field=models.CharField(blank=True, default='Admin', max_length=22, null=True),
        ),
    ]
