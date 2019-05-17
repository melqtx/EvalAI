# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0050_remove_charfield_from_challenge_slug")
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="cli_version",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="evalai-cli version",
            ),
        )
    ]