# Generated by Django 3.0.7 on 2020-10-02 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('cellphone', models.BigIntegerField()),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=1, max_length=10)),
                ('fashion', models.CharField(choices=[('General', 'General'), ('A Medida', 'A Medida')], default=1, max_length=50)),
                ('image', models.ImageField(null=True, upload_to='fashion/%Y/%m/%d/')),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Cloth',
            },
        ),
        migrations.CreateModel(
            name='DressesUniform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=1, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='uniforms/Female/dresses/%Y/%m/%d/')),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'DressesUniform',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Institution',
            },
        ),
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default='ref', max_length=10, null=True)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=1, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='uniforms/Male/pants/%Y/%m/%d/')),
                ('type', models.CharField(blank=True, choices=[('Classic Male', 'Classic Male'), ('Classic Female', 'Classic Female')], default=1, max_length=10, null=True)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Pants',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_cloth', models.DecimalField(decimal_places=2, max_digits=9)),
                ('value_work', models.DecimalField(decimal_places=2, max_digits=9)),
                ('value_threads', models.DecimalField(decimal_places=2, max_digits=8)),
                ('value_buttons', models.DecimalField(decimal_places=2, max_digits=8)),
                ('value_necks', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('value_embroidery', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('value_prints', models.DecimalField(decimal_places=2, default=0, max_digits=8, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Quotation',
            },
        ),
        migrations.CreateModel(
            name='Shields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_college', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='uniforms/shields/%Y/%m/%d/')),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Shields',
            },
        ),
        migrations.CreateModel(
            name='Shirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default='ref', max_length=10, null=True)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default=1, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='uniforms/shirts/%Y/%m/%d/')),
                ('type', models.CharField(blank=True, choices=[('Classic Male', 'Classic Male'), ('Classic Female', 'Classic Female'), ('Sport Male', 'Sport Male'), ('Sport Female', 'Sport Female')], default='', max_length=10, null=True)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Shirts',
            },
        ),
        migrations.CreateModel(
            name='UniformsSports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_uniform', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default=1, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='confma.Institution')),
                ('pants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='confma.Pants')),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Shirts')),
            ],
            options={
                'db_table': 'UniformsSports',
            },
        ),
        migrations.CreateModel(
            name='UniformsMale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='confma.Institution')),
                ('pants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Pants')),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Shirts')),
            ],
            options={
                'db_table': 'UniformsMale',
            },
        ),
        migrations.CreateModel(
            name='UniformsFemale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.DressesUniform')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='confma.Institution')),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Shirts')),
            ],
            options={
                'db_table': 'UniformsFemale',
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_now', models.DateField(auto_now_add=True)),
                ('date_return', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=5000.0, max_digits=10)),
                ('ifrental', models.SmallIntegerField(default=1)),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Client')),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Cloth')),
            ],
            options={
                'db_table': 'Rental',
            },
        ),
        migrations.CreateModel(
            name='QuotationClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Client')),
                ('quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Quotation')),
            ],
            options={
                'db_table': 'Quotation_Client',
            },
        ),
        migrations.AddField(
            model_name='quotation',
            name='client',
            field=models.ManyToManyField(through='confma.QuotationClient', to='confma.Client'),
        ),
        migrations.AddField(
            model_name='quotation',
            name='cloth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confma.Cloth'),
        ),
    ]
