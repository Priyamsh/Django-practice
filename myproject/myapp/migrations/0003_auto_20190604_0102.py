# Generated by Django 2.1.5 on 2019-06-03 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190604_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'reporter',
            },
        ),
        migrations.RemoveField(
            model_name='dreamreal',
            name='online',
        ),
        migrations.DeleteModel(
            name='Dreamreal',
        ),
        migrations.DeleteModel(
            name='Online',
        ),
        migrations.AddField(
            model_name='article',
            name='article_reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Reporter'),
        ),
    ]