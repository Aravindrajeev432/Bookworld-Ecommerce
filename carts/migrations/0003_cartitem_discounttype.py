# Generated by Django 3.1 on 2022-08-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='discounttype',
            field=models.CharField(default='pro', max_length=50),
        ),
    ]