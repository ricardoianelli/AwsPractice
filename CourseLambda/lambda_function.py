import json
import boto3
from list_function import get_items
from put_function import put_item
from update_function import update_item
from delete_function import delete_item


#TODO: improve the way I handle the events
def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table_name = 'Course'
    table = dynamodb.Table(table_name) 
    
    body = json.loads(event["body"]) if (event["body"] != None) else None
    path_params = event["pathParameters"]
    query_strings = event["queryStringParameters"]
    headers = event["headers"]
    
    http_method = event["httpMethod"]
    
    print(f"[{http_method}] Receiving request.")
    
    response = {}
    
    try:
        if (http_method == "GET"):
            response = get_items(table, query_strings)
    
        if (http_method == "POST"):
            response = put_item(table, body)
            
        if (http_method == "PATCH"):
            response = update_item(table, body, path_params)
            
        if (http_method == "DELETE"):
            response = delete_item(table, path_params)
    except Exception as e:
        print(f"[{http_method}] There was an exception during your request. Exception: {e}")
        response = {
            'statusCode': 500, #Improve depending on the exception
            'body': json.dumps(f'There was an error during your request: {e}')
        }
    finally:
        print(f"[{http_method}] Responding request. Status Code: {response.get('statusCode')}")
        return response
    
