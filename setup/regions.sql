USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS REGIONS (
    "code" text not null,
    "region_name" text,
    "region_name_alt" text,
    "latitude" numeric,
    "longitude" numeric
);
