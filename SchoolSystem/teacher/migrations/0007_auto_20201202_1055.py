# Generated by Django 3.1.3 on 2020-12-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20201202_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='pupilstoobjects',
            name='grade',
        ),
    ]
