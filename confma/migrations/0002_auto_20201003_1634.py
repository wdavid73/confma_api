# Generated by Django 3.0.7 on 2020-10-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pants',
            name='ref',
            field=models.CharField(default='ref', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shirts',
            name='ref',
            field=models.CharField(default='ref', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shirts',
            name='type',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=10, null=True),
        ),
    ]
