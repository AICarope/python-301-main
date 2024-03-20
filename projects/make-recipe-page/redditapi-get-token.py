# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.


import requests
import requests.auth

# Reddit API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'

# Step 1: Obtain an access token
client_auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
post_data = {"grant_type": "password", "username": username, "password": password}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
access_token = response.json()['access_token']

# Step 2: Make authenticated requests to the Reddit API
headers = {"Authorization": "bearer " + access_token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
print(response.json())