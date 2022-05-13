import json
from get_function import get_item


def update_item(table, body, key):
    
    current_state = get_item(table, key)
    if (current_state == None):
        return {
            'statusCode': 404
        }
    
    to_update = {}
    update_expression = "set "
    
    for attribute in body:
        to_update[f":{attribute}"] = body[attribute]
        update_expression += f"{attribute} = :{attribute},"
        
    update_expression = update_expression[:-1]
    
    print("Updating item")
    table.update_item(Key=key, UpdateExpression=update_expression,ExpressionAttributeValues=to_update)
    data = get_item(table, key)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }