# Generated by Django 3.2.9 on 2021-12-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211201_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='medicacoes',
            field=models.ManyToManyField(to='app.Horario'),
        ),
    ]
