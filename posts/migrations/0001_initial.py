# Generated by Django 3.2.9 on 2021-12-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('author', models.CharField(max_length=200)),
                ('count_likes', models.IntegerField()),
                ('published', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.ManyToManyField(to='posts.Post')),
            ],
        ),
    ]
