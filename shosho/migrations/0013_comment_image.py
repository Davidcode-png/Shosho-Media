# Generated by Django 4.0.6 on 2022-08-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shosho', '0012_threadmodel_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_pic'),
        ),
    ]