# Generated by Django 3.1.5 on 2022-03-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart1', '0002_auto_20211124_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]