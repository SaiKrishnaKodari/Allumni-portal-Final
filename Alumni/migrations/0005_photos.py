# Generated by Django 3.2 on 2021-06-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0004_posts_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
    ]
