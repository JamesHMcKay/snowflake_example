from raw_table import RawTable

ITEMS = RawTable(
    "ITEMS",
    "Item",
    "No.",
    {
        "id": str,
        "description": str,
        "vendor_item_id": str,
        "inventory_posting_group": str,
        "vendor_id": str,
        "replenishment_method": str,
        "product_group_code": str,
    },
    {
        "No.": "id",
        "Decsription": "description",
        "Vendor Item No.": "vendor_item_id",
        "Inventory Posting Group": "inventory_posting_group",
        "Vendor No.": "vendor_id",
        "Replenishment Method": "replenishment_method",
        "Product Group Dimension": "product_group_code",
    },
)


CUSTOMERS = RawTable(
    "CUSTOMERS",
    "Customer",
    "No.",
    {
        "id": str,
        "customer_name": str,
        "customer_posting_group": str,
        "sales_person_code": str,
        "customer_group_code": str,
        "region_code": str,
        "staff_code": str,
    },
    {
        "No.": "id",
        "Name": "customer_name",
        "Customer Posting Group": "customer_posting_group",
        "Salesperson Code": "sales_person_code",
        "Customer Group Dimension": "customer_group_code",
        "Region Dimension": "region_code",
        "Staff Dimension": "staff_code",
    },
)


SALES = RawTable(
    "SALES",
    "VEs",
    "Entry No.",
    {
        "entry": str,
        "item_ledger_entry": str,
        "item": str,
        "posting_date": str,
        "source": str,
        "document": str,
        "quantity": int,
        "sales": float,
        "discount": float,
        "cost": float,
        "margin": float,
    },
    {
        "Entry No.": "entry",
        "Item Ledger Entry No.": "item_ledger_entry",
        "Item No.": "item",
        "Posting Date": "posting_date",
        "Source No.": "source",
        "Document No.": "document",
        "Quantity": "quantity",
        "Sales": "sales",
        "Discount": "discount",
        "Cost of Sales": "cost",
        "Margin": "margin",
    },
)


ITEM_LEDGERS = RawTable(
    "ITEM_LEDGER",
    "ILEs",
    "Entry No.",
    {
        "entry": int,
        "item": str,
        "posting_date": str,
        "customer": str,
        "document": str,
        "external_document": str,
    },
    {
        "Entry No.": "entry",
        "Item No.": "item",
        "Posting Date": "posting_date",
        "Customer No.": "customer",
        "Document No.": "document",
        "External Document No.": "external_document",
    },
)


CUSTOMER_GROUPS = RawTable(
    "CUSTOMER_GROUPS",
    "Cust Group",
    "Code",
    {"code": str, "name": str},
    {"Code": "code", "Name": "name"},
)

REGIONS = RawTable(
    "REGIONS",
    "Region",
    "Code",
    {
        "code": str,
        "region_name": str,
        "region_name_alt": str,
        "latitude": float,
        "longitude": float,
    },
    {
        "Code": "code",
        "Name": "region_name",
        "Rename": "region_name_alt",
        "Latitude": "latitude",
        "Longitude": "longitude",
    },
)


STAFF = RawTable(
    "STAFF",
    "Staff",
    "Code",
    {"code": str, "name": str},
    {"Code": "code", "Name": "name"},
)

PRODUCT_GROUPS = RawTable(
    "PRODUCT_GROUPS",
    "Prod Group",
    "Code",
    {"code": str, "name": str},
    {"Code": "code", "Name": "name"},
)
