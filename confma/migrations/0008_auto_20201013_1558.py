# Generated by Django 3.0.7 on 2020-10-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0007_auto_20201009_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniformssports',
            name='type_uniform',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default=1, max_length=20),
        ),
    ]
