# Generated by Django 3.2.18 on 2023-03-28 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_account_number', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_bank_accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('customer_name', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('identity_number', models.CharField(max_length=255)),
                ('identity_type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('principal_amount', models.FloatField()),
                ('rate', models.FloatField()),
                ('duration', models.IntegerField()),
                ('interest', models.FloatField()),
                ('repayment_date', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_loans', to='core.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('purity', models.FloatField()),
                ('purity_metric', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('weight_metric', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_product_items', to='core.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='core.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('payment_date', models.DateTimeField()),
                ('payment_amount', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_payments', to='core.customer')),
                ('loan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_payments', to='core.loan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='loan',
            name='product_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_product_item_loans', to='core.productitem'),
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('identity_document', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('signature', models.CharField(max_length=255)),
                ('thumb', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_details', to='core.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, null=True)),
                ('updated_date', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True)),
                ('transaction_amount', models.FloatField()),
                ('transaction_date', models.DateTimeField()),
                ('bank_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_account_transactions', to='core.bankaccount')),
                ('product_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item_bank_transactions', to='core.productitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
