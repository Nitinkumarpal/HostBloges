# Generated by Django 3.1.6 on 2021-05-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Contactus',
        ),
    ]