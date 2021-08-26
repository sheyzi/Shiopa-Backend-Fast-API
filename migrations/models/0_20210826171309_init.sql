-- upgrade --
CREATE TABLE IF NOT EXISTS "currency" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "currency_code" VARCHAR(5) NOT NULL,
    "exchange_rate" INT NOT NULL,
    "symbol" VARCHAR(20) NOT NULL,
    "position" VARCHAR(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS "country" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "default_country" INT NOT NULL  DEFAULT 0,
    "currency_id" INT  UNIQUE REFERENCES "currency" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "settings" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "store_name" VARCHAR(255) NOT NULL,
    "store_tagline" VARCHAR(255),
    "store_logo" VARCHAR(500) NOT NULL,
    "copyright_text" VARCHAR(255),
    "store_address" VARCHAR(1000) NOT NULL,
    "store_phone" VARCHAR(20) NOT NULL,
    "store_email" VARCHAR(80) NOT NULL,
    "facebook_link" VARCHAR(200),
    "twitter_link" VARCHAR(200),
    "instagram_link" VARCHAR(200),
    "meta_description" VARCHAR(1000),
    "keywords" VARCHAR(1000),
    "favicon" VARCHAR(500)
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
