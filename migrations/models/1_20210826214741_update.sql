-- upgrade --
ALTER TABLE "country" ADD "delivery_fee" REAL;
-- downgrade --
ALTER TABLE "country" DROP COLUMN "delivery_fee";
