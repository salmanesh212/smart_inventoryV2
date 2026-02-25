# Fix: remove M2M 'items' from Order, restore 'order' FK on OrderItem

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0003_remove_orderitem_order_order_items'),
    ]

    operations = [
        # 1. Drop the M2M relationship that migration 0003 created
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        # 2. Re-add the ForeignKey on OrderItem pointing to Order
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='items',
                to='business_app.order',
                default=1,
            ),
            preserve_default=False,
        ),
    ]
