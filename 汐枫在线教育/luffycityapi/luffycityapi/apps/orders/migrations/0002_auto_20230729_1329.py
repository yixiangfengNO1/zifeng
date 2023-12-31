# Generated by Django 3.2.9 on 2023-07-29 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='credit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_orders', to=settings.AUTH_USER_MODEL, verbose_name='下单用户'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='fg_order',
        ),
    ]
