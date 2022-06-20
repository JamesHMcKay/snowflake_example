USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS SALES (
    "entry" TEXT NOT NULL PRIMARY KEY,
    "item_ledger_entry" TEXT,
    "item" TEXT,
    "posting_date" TEXT,
    "source" TEXT,
    "document" TEXT,
    "quantity" NUMERIC,
    "sales" NUMERIC,
    "discount" NUMERIC,
    "cost" NUMERIC,
    "margin" NUMERIC
);
