# Generated by Django 3.0.7 on 2020-09-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confma', '0003_auto_20200430_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uniforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_college', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=1, max_length=10)),
                ('fashion', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='uniforms/%Y/%m/%d')),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Uniforms',
            },
        ),
    ]