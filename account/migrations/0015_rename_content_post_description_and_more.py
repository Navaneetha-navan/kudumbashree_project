# Generated by Django 4.0.2 on 2022-03-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_post_delete_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='filename',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file'),
        ),
    ]
