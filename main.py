from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()
token_required = True
current_time = datetime.now()

with open('token_expiry.txt', 'r+') as file:
    if file.read() != '':
        file.seek(0)
        prev = file.readline()
        prev_time = datetime.strptime(prev, '%Y-%m-%d %H:%M:%S')
        
        diff = current_time - prev_time
        token_required = abs(diff) >= timedelta(hours=1)        
    
    if token_required:
        file.seek(0)
        current_time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        file.write(current_time_string)

        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        
        url = 'https://accounts.spotify.com/api/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        response = requests.post(url, headers=headers, data=data)
        token = response.json().get('access_token')
        print(token)
        with open('token.txt', 'w') as token_file:
            token_file.write(token)
            
token = None
with open('token.txt', 'r') as token_file:
    token = token_file.readline()

artist_url = sys.argv[1]
url = f'https://api.spotify.com/v1/artists/{artist_url}/top-tracks'
access_token = token
headers = {
    'Authorization': f'Bearer {access_token}'
}
response = requests.get(url, headers=headers)
data = response.json()
for track in data['tracks']:
    title = track['name']
    popularity = track['popularity']
    print(f"{title} ({popularity})")
