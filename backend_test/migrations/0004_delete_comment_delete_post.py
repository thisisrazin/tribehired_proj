# Generated by Django 4.2.4 on 2023-08-18 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_test', '0003_alter_comment_id_alter_post_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
