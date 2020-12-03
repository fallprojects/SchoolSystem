# Generated by Django 3.1.3 on 2020-12-02 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0004_auto_20201202_0915'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PupilstoObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupils', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pupils.pupils')),
                ('subjects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_subjects', to='teacher.subject')),
            ],
        ),
    ]