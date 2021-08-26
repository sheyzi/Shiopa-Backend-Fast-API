from tortoise.models import Model
from tortoise import fields


class Image(Model):
    title = fields.CharField(max_length=255)
    alt_text = fields.CharField(max_length=255, null=True)
    url = fields.CharField(
        max_length=255,
        default="https://res.cloudinary.com/sheyzisilver/image/upload/v1628729409/placeholder_rl2wsr.png",
    )


class Section(Model):
    title = fields.CharField(max_length=255)
    ordering = fields.IntField()
    image = fields.ForeignKeyField(
        model_name="models.Image",
        on_delete=fields.SET_NULL,
        null=True,
        related_name="sections",
    )
    products: fields.ReverseRelation["Product"]


class Category(Model):
    name = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=255)
    image = fields.ForeignKeyField(
        model_name="models.Image",
        on_delete=fields.SET_NULL,
        null=True,
        related_name="categories",
    )

    parent: fields.ForeignKeyNullableRelation["Category"] = fields.ForeignKeyField(
        "models.Category", related_name="children_categories", null=True
    )
    children_categories: fields.ReverseRelation["Category"]
    products: fields.ReverseRelation["Product"]


class Product(Model):
    category = fields.ForeignKeyField(
        model_name="models.Category", related_name="products", on_delete=fields.RESTRICT
    )
    section = fields.ForeignKeyField(
        model_name="models.Section", related_name="products", on_delete=fields.RESTRICT
    )
    name = fields.CharField(max_length=255)
    slug = fields.CharField(max_length=255)
    description = fields.CharField(max_length=1000, null=True)
    additional_info = fields.CharField(max_length=1000, null=True)
    sku = fields.CharField(max_length=255, null=True)
    main_image = fields.ForeignKeyField(
        model_name="models.Image",
        on_delete=fields.SET_NULL,
        null=True,
        related_name="products",
    )
    other_images = fields.ManyToManyField(
        model_name="models.Image", related_name="products_others_image"
    )
    price = fields.FloatField()
    discount_price = fields.FloatField(null=True)
    stock = fields.IntField(null=True)
    available_to_purchase = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    products: fields.ReverseRelation["ProductReview"]

    def discount_percentage(self):
        if not self.discount_price:
            # Check if there is a discount price
            # If there is no discount price return None
            return None

        # Calculate the percentage if discount price is found
        percentage = (self.discount_price / self.price) * 100
        return percentage

    class PydanticMeta:
        computed = ["discount_percentage"]


class ProductReview(Model):
    product = fields.ForeignKeyField(
        model_name="models.Product", related_name="reviews"
    )
    user = fields.ForeignKeyField(model_name="models.Product")
    comment = fields.CharField(max_length=1000)
    rating = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Coupon(Model):
    coupon_code = fields.CharField(max_length=255)
    coupon_type = fields.CharField(max_length=255, null=True)
    coupon_amount = fields.FloatField(null=True)
    coupon_amount = fields.IntField(null=True)
    active = fields.BooleanField(default=True)
    num_available = fields.IntField()
    num_used = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
