# Generated by Django 4.1 on 2022-08-26 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=20)),
                ('edad', models.IntegerField(max_length=5)),
                ('fecha_nacimiento', models.DateField(max_length=20)),
            ],
        ),
    ]
