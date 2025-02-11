flame_sensor_1 = None


import sys, os
HOME        = os.path.expanduser('~')
RPI_HOME    = HOME + '/RPI/'
GROK_HOME   = HOME + '/Desktop/Grok-Downloads/'
sys.path.insert(1, RPI_HOME)
from file_watcher import FileWatcher, device_sensor
from grok_library import check_with_simulator,check_with_simulator2, device, sim_device, pin, GrokLib
import threading
grokLib = GrokLib()

device['applicationIdentifier'] = str(os.path.splitext(os.path.basename(__file__))[0])
device['mobile_messages'] = list()

def simulate(list_of_sensors):
    if list_of_sensors is not None:
        global sim_device
        sim_device = list_of_sensors
def startListener1():
    FileWatcher(simulate, 'simulation.json', RPI_HOME, 'config_file')
thread1 = threading.Thread(target=startListener1, args=())
thread1.daemon=True
thread1.start()


import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
from cv2 import *
cam_port = 0
GPIO.setup((7), GPIO.IN)
GPIO.setup((16), GPIO.OUT)
GPIO.setup((10), GPIO.OUT)
GPIO.setup((23), GPIO.OUT)
GPIO.output((23), GPIO.HIGH)
while True:
  flame_sensor_1 = (GPIO.input(7))
  flame_sensor_1 = check_with_simulator2(flame_sensor_1,'flame_sensor_1', sim_device)
  if flame_sensor_1 == 1:
    print('FIRE DETECTED')
    device["mobile_messages"].append({'type' : 'text','value' : 'FIRE DETECTED','color' : '#ff0000'})
    cam = VideoCapture(cam_port)
    result, image = cam.read()
    if result:
    	imwrite("/home/pi/Desktop/Grok-Downloads/image.jpg", image)
    cam.release()
    image_url = grokLib.upload_image('/home/pi/Desktop/Grok-Downloads/image.jpg')
    device['mobile_messages'].append({'type' : 'image','source' : image_url,'state' : True})

    device_sensor(device)
    device["mobile_messages"] = []
    GPIO.output(16, True)
    GPIO.output(10, True)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(1)
  elif flame_sensor_1 == 0:
    print('NO FIRE DETECTED')
    device["mobile_messages"].append({'type' : 'text','value' : 'NO FIRE DETECTED','color' : '#33ffff'})

    device_sensor(device)
    device["mobile_messages"] = []
    GPIO.output(16, False)
    GPIO.output(10, False)
    GPIO.output(23, GPIO.LOW)
    time.sleep(1)
