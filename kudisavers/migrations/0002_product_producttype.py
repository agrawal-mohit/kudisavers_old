# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kudisavers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(null=True, related_name='products', to='kudisavers.ProductType'),
            preserve_default=True,
        ),
    ]
