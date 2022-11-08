# Generated by Django 4.1.3 on 2022-11-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeeklyRecords',
            new_name='DailyRecord',
        ),
        migrations.RenameModel(
            old_name='Days',
            new_name='Day',
        ),
        migrations.AddConstraint(
            model_name='dailyrecord',
            constraint=models.UniqueConstraint(fields=('habit', 'date_recorded'), name='unique_daily_record'),
        ),
    ]
