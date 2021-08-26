from shiopa_backend.apps.users.models import User, ShippingAddress
from shiopa_backend.apps.products.models import Product, Coupon
from tortoise.models import Model
from tortoise import fields


class Order(Model):
    user = fields.ForeignKeyField(
        model_name="models.User",
        related_name="orders",
        on_delete=fields.SET_NULL,
        null=True,
    )
    shipping_address = fields.ForeignKeyField(
        model_name="models.ShippingAddress",
        related_name="orders",
        on_delete=fields.SET_NULL,
        null=True,
    )
    total_payment = fields.FloatField()
    payment_status = fields.CharField(max_length=255, default="PENDING")
    status = fields.CharField(max_length=255, default="PENDING")
    status = fields.CharField(max_length=255, default="PENDING_APPROVAL")
    note = fields.CharField(max_length=1000, default="PENDING_APPROVAL", null=True)
    coupon = fields.ForeignKeyField(
        model_name="models.Coupon",
        related_name="orders",
        on_delete=fields.SET_NULL,
        null=True,
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    items: fields.ReverseRelation["OrderItem"]


class OrderItem(Model):
    product = fields.ForeignKeyField(
        model_name="models.Product",
        related_name="orders",
        on_delete=fields.SET_NULL,
        null=True,
    )
    order = fields.ForeignKeyField(
        model_name="models.Order",
        related_name="items",
        on_delete=fields.SET_NULL,
        null=True,
    )
    quantity = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
