# Generated by Django 5.2 on 2025-04-04 20:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gul', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(max_length=255, verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='order',
            name='receipt',
            field=models.FileField(blank=True, null=True, upload_to='receipts/', verbose_name='Receipt'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10, verbose_name='Status'),
        ),
    ]
