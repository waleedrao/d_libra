# Generated by Django 4.0.3 on 2022-05-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0017_user_otp_user_otpcount_user_otpstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passwordstatus',
            field=models.CharField(default='False', max_length=10),
        ),
    ]