# Generated by Django 3.2.9 on 2021-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(max_length=5)),
                ('numero_conta', models.CharField(max_length=10)),
                ('saldo', models.CharField(max_length=20)),
            ],
        ),
    ]
