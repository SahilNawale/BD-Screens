# Generated by Django 4.1.1 on 2022-11-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_bookedticket_bookedseat'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazorpayPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField(default=100)),
                ('payment_order_id', models.CharField(max_length=100)),
            ],
        ),
    ]
