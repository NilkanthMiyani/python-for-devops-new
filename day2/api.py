import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Server url (API)

response = requests.get(url=api_url)

print(response.json())

print(dir(response))

for k,v in response.json().items():
    if k == "completed":
        if v == False:
            print("Task is not completed")
    if k == "userId":
        if v in [1,2,3,4,5]:
            print("User found")

