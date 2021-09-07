# Generated by Django 3.2.6 on 2021-09-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('start_date', models.CharField(default='01-01-2021', max_length=50)),
                ('end_date', models.CharField(default='31-12-2021', max_length=50)),
                ('hours', models.CharField(default='50', max_length=50)),
            ],
        ),
    ]
