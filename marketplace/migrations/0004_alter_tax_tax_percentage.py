# Generated by Django 4.2.3 on 2023-08-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_alter_tax_options_alter_tax_tax_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tax_percentage',
            field=models.DecimalField(decimal_places=3, max_digits=5, verbose_name='Tax Percentage (%)'),
        ),
    ]
