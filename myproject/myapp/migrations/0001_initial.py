# Generated by Django 2.1.5 on 2019-06-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=75)),
                ('phoneno', models.IntegerField()),
                ('mail', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
    ]