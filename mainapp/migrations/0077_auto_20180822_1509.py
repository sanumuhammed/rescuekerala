# Generated by Django 2.1 on 2018-08-22 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0076_auto_20180822_1220"),
    ]

    operations = [
        migrations.AddField(
            model_name="csvbulkupload",
            name="camp",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="mainapp.RescueCamp",),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="csvbulkupload", name="is_completed", field=models.BooleanField(default=False),
        ),
    ]
