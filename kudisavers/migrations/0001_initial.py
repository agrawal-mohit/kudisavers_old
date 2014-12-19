# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('blockName', models.CharField(max_length=50)),
                ('catName', models.CharField(max_length=50)),
                ('catUrl', models.URLField(max_length=100)),
                ('prodTypeName', models.CharField(max_length=50)),
                ('prodTypeUrl', models.URLField(max_length=100)),
                ('prodName', models.CharField(max_length=50)),
                ('prodUrl', models.URLField(max_length=100)),
                ('prodDesc', models.TextField(max_length=500)),
                ('prodProperties', models.TextField(max_length=500)),
                ('reviews', models.TextField()),
                ('imageLink', models.URLField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('offerPrice', models.FloatField()),
                ('availability', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True)),
                ('attribute', models.ForeignKey(to='kudisavers.ProductAttribute')),
                ('product', models.ForeignKey(related_name='details', to='kudisavers.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('Category', models.ForeignKey(related_name='categories', to='kudisavers.Category')),
                ('parent', models.ForeignKey(blank=True, related_name='product_types', to='kudisavers.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='Section',
            field=models.ForeignKey(related_name='categories', to='kudisavers.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, related_name='children', to='kudisavers.Category', null=True),
            preserve_default=True,
        ),
    ]
