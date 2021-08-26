-- upgrade --
CREATE TABLE IF NOT EXISTS "order" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "total_payment" REAL NOT NULL,
    "payment_status" VARCHAR(255) NOT NULL  DEFAULT 'PENDING',
    "status" VARCHAR(255) NOT NULL  DEFAULT 'PENDING_APPROVAL',
    "note" VARCHAR(1000)   DEFAULT 'PENDING_APPROVAL',
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "coupon_id" INT REFERENCES "coupon" ("id") ON DELETE SET NULL,
    "shipping_address_id" INT REFERENCES "shippingaddress" ("id") ON DELETE SET NULL,
    "user_id" INT REFERENCES "user" ("id") ON DELETE SET NULL
);;
CREATE TABLE IF NOT EXISTS "orderitem" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "quantity" INT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "order_id" INT REFERENCES "order" ("id") ON DELETE SET NULL,
    "product_id" INT REFERENCES "product" ("id") ON DELETE SET NULL
);-- downgrade --
DROP TABLE IF EXISTS "order";
DROP TABLE IF EXISTS "orderitem";
