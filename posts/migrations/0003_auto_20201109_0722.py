# Generated by Django 3.0.6 on 2020-11-09 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='rates',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.PostsRates'),
        ),
    ]
