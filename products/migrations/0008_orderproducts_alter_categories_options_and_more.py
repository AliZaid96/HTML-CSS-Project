# Generated by Django 4.1.1 on 2022-10-30 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_total', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Order Products',
            },
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='customerorder',
            options={'verbose_name_plural': 'Customer Orders'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='status',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='sum_amount',
        ),
        migrations.RemoveField(
            model_name='customerorder',
            name='website_customer',
        ),
        migrations.AddField(
            model_name='customerorder',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='order_id',
            field=models.CharField(default=uuid.uuid4, max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='Order #'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='total_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterModelTable(
            name='categories',
            table=None,
        ),
        migrations.AlterModelTable(
            name='customerorder',
            table=None,
        ),
        migrations.AlterModelTable(
            name='products',
            table=None,
        ),
        migrations.DeleteModel(
            name='WebsiteUser',
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='products.customerorder'),
        ),
        migrations.AddField(
            model_name='orderproducts',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.products'),
        ),
    ]
