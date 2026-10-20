import requests

response = requests.get("https://api.github.com")
print(response.status_code)

print("This time I am serious about the API")
print(response.text)