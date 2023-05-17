# Generated by Django 4.2.1 on 2023-05-14 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DownBus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NowDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_type', models.CharField(choices=[('WEEK', '주중'), ('SAT', '토요일'), ('SUN', '일요일/공휴일')], max_length=8, verbose_name='요일')),
            ],
        ),
        migrations.AddField(
            model_name='buslist',
            name='day_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='DownBus.nowday', verbose_name='요일'),
        ),
    ]