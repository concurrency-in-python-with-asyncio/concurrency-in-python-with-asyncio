import requests

response = requests.get('https://www.example.com')

headers = [f'{key}: {response.headers[key]}' for key in response.headers]

formatted_headers = '\n'.join(headers)

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)
