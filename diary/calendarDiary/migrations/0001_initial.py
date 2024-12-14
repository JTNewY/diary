# Generated by Django 5.1.3 on 2024-12-05 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_name', models.CharField(max_length=100, verbose_name='공휴일 이름')),
                ('H_date', models.DateField(verbose_name='공휴일 날짜')),
                ('H_memo', models.CharField(blank=True, max_length=255, verbose_name='공휴일 설명')),
                ('H_country', models.CharField(choices=[('KR', 'South Korea'), ('US', 'United States'), ('JP', 'Japan')], max_length=2, verbose_name='국가코드')),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
                'ordering': ['H_date'],
            },
        ),
        migrations.CreateModel(
            name='CalendarDiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('color', models.CharField(default='#FFFFFF', max_length=7)),
                ('status', models.CharField(choices=[('planned', 'Planned'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='planned', max_length=50)),
                ('content', models.TextField(blank=True)),
                ('notification_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diaries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
