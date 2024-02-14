import time 
from gpiozero import DistanceSensor

print('Prepare GPIO pins')
sensor_l = DistanceSensor(echo=17, trigger= 27, queue_len=2)
sensor_r = DistanceSensor(echo=5, trigger= 6, queue_len=2)