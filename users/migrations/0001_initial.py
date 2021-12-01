# Generated by Django 3.2.9 on 2021-11-14 06:21

import core.models
from django.db import migrations, models
import django_lifecycle.mixins
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=core.models.path_and_rename)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('about_me', models.CharField(blank=True, max_length=1024)),
                ('sex', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('ANOTHER', 'Another')], default='', max_length=10)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_joined'],
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]