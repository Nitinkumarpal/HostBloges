# Generated by Django 3.1.6 on 2021-05-07 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogers', '0002_auto_20210506_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('security', models.CharField(max_length=140)),
                ('sanswer', models.CharField(max_length=150)),
            ],
        ),
    ]
