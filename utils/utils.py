"""
 Created by harshit on 8/9/2019
"""
import json

jsontype = "application/json"
formtype = "multipart/form-data; boundary=----WebKitFormBoundaryqERAN6VL6ZWSQ4wz"


def request_type(request):
    if request.content_type == jsontype:
        data = json.loads(request.body)
    else:
        data = request.POST
    print(data)
    return data