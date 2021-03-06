# Generated by Django 3.1.7 on 2021-04-06 09:29

import django.contrib.sites.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sites.site')),
                ('settings', models.JSONField(blank=True, default={})),
                ('port', models.PositiveIntegerField(null=True)),
                ('protocol', models.CharField(default='http', max_length=5)),
            ],
            bases=('sites.site',),
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
