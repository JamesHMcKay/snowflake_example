USE DATABASE SALES_REPORTING;
CREATE TABLE IF NOT EXISTS REGIONS (
    "code" TEXT NOT NULL PRIMARY KEY,
    "region_name" TEXT,
    "region_name_alt" TEXT,
    "latitude" NUMERIC,
    "longitude" NUMERIC
);
