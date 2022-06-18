# Generated by Django 4.0.5 on 2022-06-16 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='adress',
            field=models.CharField(blank=True, help_text='Enter user address', max_length=500, null=True, verbose_name='User address'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Enter chosen courses', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.courses', verbose_name='Courses'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(blank=True, help_text='Enter user phone number', max_length=500, null=True, verbose_name='User phone number'),
        ),
    ]