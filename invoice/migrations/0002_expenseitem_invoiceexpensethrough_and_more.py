# Generated by Django 4.1 on 2022-08-10 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceExpenseThrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.expenseitem')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
        migrations.DeleteModel(
            name='Expense_item',
        ),
        migrations.AddField(
            model_name='expenseitem',
            name='invoice',
            field=models.ManyToManyField(related_name='invoice', through='invoice.InvoiceExpenseThrough', to='invoice.invoice'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='expense_items',
            field=models.ManyToManyField(related_name='expense_items', through='invoice.InvoiceExpenseThrough', to='invoice.expenseitem'),
        ),
    ]
