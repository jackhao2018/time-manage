# Generated by Django 3.1.1 on 2021-03-21 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('logout', models.PositiveIntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Collects',
            fields=[
                ('collect_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('strategy_id', models.IntegerField()),
            ],
            options={
                'db_table': 'collects',
                'managed': True,
                'unique_together': {('user_id', 'strategy_id')},
            },
        ),
    ]