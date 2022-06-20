USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS ITEM_LEDGER (
    "entry" TEXT NOT NULL PRIMARY KEY,
    "item" TEXT,
    "posting_date" TEXT,
    "customer" TEXT,
    "document" TEXT,
    "external_document" TEXT
);
