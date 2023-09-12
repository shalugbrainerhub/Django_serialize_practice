import requests

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='allemployeejsonview'

# response_result=requests.delete(BASE_URL+ENDPOINT)
# data=response_result.json()
# print(data)

def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id)
    print(resp.status_code)
    # print(resp.json())
    print(resp.json())
# id=input('Enter the id for the employee:')
# get_resource(id)

def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
get_all()


