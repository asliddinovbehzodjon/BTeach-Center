# Generated by Django 4.0.5 on 2022-06-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_clients_adress_alter_clients_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='t_id',
            field=models.IntegerField(help_text='Enter user telegram id', verbose_name='User Telegram Id'),
        ),
    ]
