# Generated by Django 3.2.6 on 2021-08-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('num_pages', models.IntegerField(default=0)),
                ('published_Date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('color', models.CharField(blank=True, max_length=32, null=True)),
                ('isbn13', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
