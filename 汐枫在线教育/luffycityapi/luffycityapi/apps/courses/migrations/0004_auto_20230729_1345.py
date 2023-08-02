# Generated by Django 3.2.9 on 2023-07-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='积分'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='课程原价'),
        ),
    ]
