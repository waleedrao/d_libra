# Generated by Django 4.0.3 on 2022-05-20 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0015_contentrating_author_courserating_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PriorityType', models.CharField(choices=[('highpriority', 'highpriority'), ('reviewlist', 'reviewlist'), ('futureread', 'futureread')], default='highpriority', max_length=20)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapi.user')),
                ('content_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapi.reviewmodel')),
            ],
        ),
    ]