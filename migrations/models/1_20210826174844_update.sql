-- upgrade --
CREATE TABLE IF NOT EXISTS "shippingaddress" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "receiver_name" VARCHAR(255) NOT NULL,
    "receiver_phone" VARCHAR(255) NOT NULL,
    "receiver_email" VARCHAR(255) NOT NULL,
    "company_name" VARCHAR(255),
    "street_address1" VARCHAR(500) NOT NULL,
    "street_address2" VARCHAR(500),
    "closest_landmark" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL,
    "postal_code" VARCHAR(255),
    "state_division" VARCHAR(255),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "country_id" INT NOT NULL REFERENCES "country" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);;
CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "avatar" VARCHAR(255) NOT NULL  DEFAULT 'https://res.cloudinary.com/sheyzisilver/image/upload/v1629983532/Shiopa/default-avatar_cbbfaz.png',
    "note" VARCHAR(255) NOT NULL,
    "is_active" INT NOT NULL  DEFAULT 1,
    "is_admin" INT NOT NULL  DEFAULT 0,
    "date_joined" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);-- downgrade --
DROP TABLE IF EXISTS "shippingaddress";
DROP TABLE IF EXISTS "user";
