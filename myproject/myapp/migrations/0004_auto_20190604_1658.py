# Generated by Django 2.1.5 on 2019-06-04 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190604_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_reporter',
            new_name='reporter',
        ),
    ]
