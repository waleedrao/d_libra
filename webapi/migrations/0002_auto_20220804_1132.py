# Generated by Django 3.2.5 on 2022-08-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, help_text='slug is an Unique value for singel categories page URL, Same as category Name'),
        ),
        migrations.AlterField(
            model_name='recentlyviewcontent',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]