# Generated by Django 4.0.3 on 2022-04-05 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0003_alter_reviewmodel_meta_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewmodel',
            old_name='ogp',
            new_name='OGP',
        ),
    ]