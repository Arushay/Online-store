# Generated by Django 3.1.6 on 2021-03-20 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupzy', '0003_orders_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
