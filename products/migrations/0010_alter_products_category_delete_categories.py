# Generated by Django 4.1.1 on 2022-10-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_customerorder_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('pz', 'Pizza'), ('sp', 'Spaghetti'), ('sw', 'Sweets')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]