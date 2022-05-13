import json
from boto3.dynamodb.conditions import Attr

def get_items(table, filters):
        
    conditions = None
    response = None
    
    if (filters != None):
        for filter in filters:
            if (conditions == None):
                conditions = Attr(filter).eq(filters[filter])
            else:
                conditions = conditions & Attr(filter).eq(filters[filter]) 
    
    if (conditions != None):
        print("Scanning with filters")
        response = table.scan(FilterExpression = conditions)
    else:
        print("Scanning everybody")
        response = table.scan()
    
    if (len(response["Items"]) > 0):
        return {
            'statusCode': 200,
            'body': json.dumps(response["Items"])
        }
    else:
        return {
            'statusCode': 404,
            'body': "No data found with those filters"
        }
