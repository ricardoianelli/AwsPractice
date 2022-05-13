import json
from get_function import get_item


def put_item(table, body):
  
    to_include = {
        'courseId': body["courseId"],
        'courseName': body["courseName"],
        'teacherName': body["teacherName"],
        'studendId': body["studendId"],
        'studentName': body["studentName"],
    }
    
    current_state = get_item(table, {'courseId': body["courseId"], 'studendId': body["studendId"]})
    print("current_state: "+ json.dumps(current_state))
    if (current_state != None):
        return {
            'statusCode': 409
        }
    
    print("Putting new item")
    data = table.put_item(Item=body)
    return {'statusCode': 201}
