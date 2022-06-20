USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS ITEMS (
    "id" TEXT NOT NULL PRIMARY KEY,
    "description" TEXT,
    "vendor_item_id" TEXT,
    "inventory_posting_group" TEXT,
    "vendor_id" TEXT,
    "replenishment_method" TEXT,
    "product_group_code" TEXT
);
