# Generated by Django 4.2.2 on 2023-06-09 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('business_field', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('budget', models.IntegerField()),
                ('currency', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wid', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.company')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.deal')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.deal')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.employee')),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.employee'),
        ),
    ]
