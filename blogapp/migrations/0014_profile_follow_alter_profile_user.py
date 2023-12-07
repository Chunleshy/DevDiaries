# Generated by Django 4.2.7 on 2023-12-06 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0013_remove_profile_follow_alter_blog_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
