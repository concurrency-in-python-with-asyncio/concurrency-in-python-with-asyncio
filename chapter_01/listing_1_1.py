import requests

response = requests.get('https://www.example.com')

headers = [f'{key}: {header}' for key, header in response.headers.items()]

formatted_headers = '\n'.join(headers)

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)
