# Generated by Django 5.0 on 2023-12-06 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
