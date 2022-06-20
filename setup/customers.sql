USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    "id" TEXT NOT NULL PRIMARY KEY,
    "customer_name" TEXT,
    "customer_posting_group" TEXT,
    "sales_person_code" TEXT,
    "customer_group_code" TEXT,
    "region_code" TEXT,
    "staff_code" TEXT
);
