# Generated by Django 3.1.3 on 2020-12-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20201202_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='pupilstoobjects',
            name='grade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]