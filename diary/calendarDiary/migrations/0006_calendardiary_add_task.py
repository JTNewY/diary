# Generated by Django 5.1.3 on 2024-12-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarDiary', '0005_remove_event_description_event_end_date_note_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendardiary',
            name='add_task',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]