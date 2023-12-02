# HumanFactorsLightingProject
Home lighting utilizing a raspberry pi for a self directed project in human factors class.

# How To Setup Project
## Switch
1. Clone project onto a raspberry pi - Project was developed on a raspberry pi 3b+
2. Install libraries `python3 -m install -r requirements.txt`
3. Attatch switch as shown on the raspberry pi website in the gpiozero documentation

## Home Assistant
1. Install Home Assistant onto a raspberry pi
2. Create automations to perform the commands requested by endpoints in lightcontroller.py
3. Create triggets for the endpoints in light controller.py to envoke the automations
4. Add smart lights to home automation

## Running Software
1. ssh into the raspberry pi
2. go into the main project directory

### button driven
3. run the command `python3 LightSwitchApplication.py` this will control the lights via the switch
### keyboard driven
3. run the command `python3 LightSwitchApplication.py -k` this will control the lights via the spacebar

