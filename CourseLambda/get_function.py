import json

def get_item(table, key):
    print(f"Getting item using key {json.dumps(key)}")
    response = table.get_item(Key=key)
    return response.get("Item")