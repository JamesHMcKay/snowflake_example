from dataclasses import dataclass


@dataclass
class RawTable:
    """
    RawTable class
    """

    name: str
    sheet_name: str
    primary_key: str
    schema: dict
    columns: dict
