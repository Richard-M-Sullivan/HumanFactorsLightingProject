import constants
import json
import requests
import time

class LightController:
    def __init__(self):
        self.base_url = 'http://homeassistant.local:8123/api/'
        self.key = constants.API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.key}',
            'content-type': 'application/json',
        }

        self.endpoints = {
                'get_state':'states', 
                'toggle':'events/toggle', 
                'brightness':'events/brightness', 
                'red':'events/red', 
                'orange':'events/orange', 
                'yellow':'events/yellow', 
                'green':'events/green', 
                'blue':'events/blue', 
                'purple':'events/purple', 
                'pink':'events/pink', 
                'white':'events/white', 
        }

        def get_key(self):
            pass

        def trigger_endpoint(self, endpoint):
            if endpoint == 'get_state':
                response = requests.get(base_url+self.endpoints[endpoint], headers=header)
            else:
                response = requests.post(base_url+self.endpoints[endpoint], headers=header)

            return response


# get data from system
response = requests.get(base_url+get_state, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

# toggle the light off
response = requests.post(base_url+post_toggle, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

# toggle the light on 
response = requests.post(base_url+post_toggle, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

# cycle through the colors
response = requests.post(base_url+post_white, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_red, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_orange, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_blue, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_pink, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_yellow, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_purple, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_white, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_blue, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

time.sleep(1)

response = requests.post(base_url+post_red, headers=headers)
print(json.dumps(json.loads(response.text), indent=4))

