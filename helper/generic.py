import random

def createResponse(success=True, status_code=200, message="-", data=None):
    response = {
        "success" : success,
        "status_code" : status_code,
        "message" : message
    }

    if data != None:
        response["data"] = data
    
    return response

def generateRandomNumber(length=3):
    
    random_number = ""
    for i in range(5):
        random_number += str(random.randint(0,9))
    
    return random_number