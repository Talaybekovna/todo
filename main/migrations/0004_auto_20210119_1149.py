# Generated by Django 3.1.3 on 2021-01-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210118_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookstore',
            name='year',
            field=models.CharField(max_length=50),
        ),
    ]
