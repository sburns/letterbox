# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
                ('created_ts', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('read', models.BooleanField(default=False, verbose_name='read')),
                ('archived', models.BooleanField(default=False, verbose_name='archived')),
                ('recipient', models.ForeignKey(related_name='recieved_notices', verbose_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sent_notices', verbose_name='sender', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created_ts'],
                'verbose_name': 'notice',
                'verbose_name_plural': 'notices',
            },
        ),
    ]
