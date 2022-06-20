USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS SALES (
    "entry" text not null,
    "item_ledger_entry" text,
    "item" text,
    "posting_date" text,
    "source" text,
    "document" text,
    "quantity" numeric,
    "sales" numeric,
    "discount" numeric,
    "cost" numeric,
    "margin" numeric
);
