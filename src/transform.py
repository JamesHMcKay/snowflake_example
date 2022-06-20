def fix_trailing_decimals(data):
    """
    Due to data coming from Excel there is some funny stuff with decimals.
    """
    return data.replace(r".0$", "", regex=True)


def fix_types(data, schema):
    for col, type_ in schema.items():
        data[col] = data[col].astype(type_)
    return data


def set_column_names(data, columns):
    return data.rename(columns=columns)
