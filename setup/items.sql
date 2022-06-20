USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS ITEMS (
    "id" text not null,
    "description" text,
    "vendor_item_id" text,
    "inventory_posting_group" text,
    "vendor_id" text,
    "replenishment_method" text,
    "product_group_code" text
);
