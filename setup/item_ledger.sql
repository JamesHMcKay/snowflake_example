USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS ITEM_LEDGER (
    "entry" text not null,
    "item" text,
    "posting_date" text,
    "customer" text,
    "document" text,
    "external_document" text
);
