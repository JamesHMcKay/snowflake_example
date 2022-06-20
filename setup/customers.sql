USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    "id" text not null,
    "customer_name" text,
    "customer_posting_group" text,
    "sales_person_code" text,
    "customer_group_code" text,
    "region_code" text,
    "staff_code" text
);
