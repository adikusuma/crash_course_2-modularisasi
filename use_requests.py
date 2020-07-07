import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success response =  {response.status_code}')
        print(f'content = {response.text}')
    else:
        print(f'woops, ada kesalahan request {response.status_code}')
except Exception as e:
    print('There is an error', e)

print('program ended')

