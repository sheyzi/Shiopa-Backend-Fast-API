from shiopa_backend.apps.store.models import Country
from tortoise.models import Model
from tortoise import fields


class User(Model):
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)
    avatar = fields.CharField(
        max_length=255,
        default="https://res.cloudinary.com/sheyzisilver/image/upload/v1629983532/Shiopa/default-avatar_cbbfaz.png",
    )
    note = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    is_admin = fields.BooleanField(default=False)
    date_joined = fields.DatetimeField(auto_now_add=True)


class ShippingAddress(Model):
    user = fields.ForeignKeyField(
        "models.User", related_name="shipping_addresses", on_delete=fields.CASCADE
    )
    receiver_name = fields.CharField(max_length=255)
    receiver_phone = fields.CharField(max_length=255)
    receiver_email = fields.CharField(max_length=255)
    company_name = fields.CharField(max_length=255, null=True)
    street_address1 = fields.CharField(max_length=500)
    street_address2 = fields.CharField(max_length=500, null=True)
    closest_landmark = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)
    postal_code = fields.CharField(max_length=255, null=True)
    state_division = fields.CharField(max_length=255, null=True)
    country = fields.ForeignKeyField(
        "models.Country", related_name="shipping_addresses", on_delete=fields.CASCADE
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
