# Generated by Django 5.0.6 on 2024-05-10 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0009_livelihood_livelihooddetail_livelihoodimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CultureDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_subtext', models.TextField()),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.culture')),
            ],
        ),
        migrations.CreateModel(
            name='CultureImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cultures/')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=100)),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.culture')),
            ],
        ),
    ]
