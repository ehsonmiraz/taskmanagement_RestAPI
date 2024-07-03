import requests

# URL for the registration endpoint
url = 'http://127.0.0.1:8000/api/accounts/register/'

# User data
data = {
    'username': 'new_user',
    'password': 'password123'
}

# Make the POST request to register the user
response = requests.post(url, json=data)

# Print the response
if response.status_code == 201:
    print('Registration successful!')
else:
    print(f'Registration failed: {response.status_code}')
    print(response.json())
