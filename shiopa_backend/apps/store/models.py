from tortoise import fields
from tortoise.models import Model


class Settings(Model):
    store_name = fields.CharField(max_length=255)
    store_tagline = fields.CharField(max_length=255, null=True)
    store_logo = fields.CharField(max_length=500)
    copyright_text = fields.CharField(max_length=255, null=True)
    store_address = fields.CharField(max_length=1000)
    store_phone = fields.CharField(max_length=20)
    store_email = fields.CharField(max_length=80)
    facebook_link = fields.CharField(max_length=200, null=True)
    twitter_link = fields.CharField(max_length=200, null=True)
    instagram_link = fields.CharField(max_length=200, null=True)
    meta_description = fields.CharField(max_length=1000, null=True)
    keywords = fields.CharField(max_length=1000, null=True)
    favicon = fields.CharField(max_length=500, null=True)


class Currency(Model):
    name = fields.CharField(max_length=255)
    currency_code = fields.CharField(max_length=5)
    exchange_rate = fields.IntField()
    symbol = fields.CharField(max_length=20)
    position = fields.CharField(max_length=10)


class Country(Model):
    name = fields.CharField(max_length=255)
    default_country = fields.BooleanField(default=False)
    delivery_fee = fields.FloatField(null=True)
    currency: fields.OneToOneRelation[Currency] = fields.OneToOneField(
        model_name="models.Currency",
        related_name="country",
        on_delete=fields.SET_NULL,
        null=True,
    )
