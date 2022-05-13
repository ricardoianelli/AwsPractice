from get_function import get_item


def delete_item(table, key):
    
    current_state = get_item(table, key)
    if (current_state == None):
        return {'statusCode': 404}

    print("Deleting item")
    data = table.delete_item(Key=key)
    return {'statusCode': 200}