# Generated by Django 4.2.7 on 2023-11-28 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_alter_blog_created_alter_blog_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='thumnail',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='validity',
        ),
    ]