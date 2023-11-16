import constants
import json
import requests
import time

base_url = 'http://homeassistant.local:8123/api/'
key = constants.API_KEY
_headers = {
    'Authorization': f'Bearer {key}',
    'content-type': 'application/json',
}

endpoints = {
    'get_state':'states', 
    'off':'events/off',
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


def trigger_endpoint(endpoint):
    if endpoint == 'get_state':
        response = requests.get(base_url+endpoints[endpoint],headers=_headers)
    else:
        response = requests.post(base_url+endpoints[endpoint], headers=_headers)

    return response


if __name__ == '__main__':

    def brightness_flow():
        colors = ['red','orange','yellow','green','blue','purple','pink']
        for color in colors:
            #reset brightness
            trigger_endpoint('off')
            time.sleep(0.6)

            #set a color
            trigger_endpoint(color)
            time.sleep(0.3)


    # get data from system
    response = trigger_endpoint('get_state')
    print(json.dumps(json.loads(response.text), indent=4))

    # cycle through the colors
    brightness_flow()

