# Generated by Django 3.1.1 on 2020-09-19 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
