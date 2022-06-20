CREATE OR REPLACE TASK GENERATE_TOTALS
    SCHEDULE = 'USING CRON 0 * * * * UTC'
AS
Insert into TOTALS
SELECT
    b."inventory_posting_group",
    sum(a."sales") as "sales",
    sum(a."quantity") as "quantity",
    sum(a."margin") as "margin",
    TO_TIMESTAMP(current_timestamp()) as "processing_timestamp"
FROM
    SALES as a
    LEFT JOIN
    ITEMS as b
    ON a."item" = b."id"
GROUP BY
    b."inventory_posting_group";
ALTER TASK GENERATE_TOTALS RESUME;
