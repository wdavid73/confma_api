# Generated by Django 3.0.7 on 2020-10-05 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0002_auto_20201003_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='dressesuniform',
            name='ref',
            field=models.CharField(default='ref', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pants',
            name='type',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=10, null=True),
        ),
    ]