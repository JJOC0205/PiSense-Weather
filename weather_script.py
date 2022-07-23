#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer
BUCKET_NAME = 'Bucket Name Here'
BUCKET_KEY = 'Bucket Key Here'
ACCESS_KEY = 'Access Key Here'
sense = SenseHat()
logger=Streamer(bucket_name=BUCKET_NAME,bucket_key = BUCKET_KEY,access_key=ACCESS_KEY)
sense.clear()
try:
    while True:
        temp = sense.get_temperature()
        temp = 1.8 * round(temp,1) + 32
        temp = round(temp,1)
        logger.log("Temperature F",temp)

        hummidity = sense.get_humidity()
        humidity = round(hummidity,1)
        logger.log("Humidiity :",humidity)

        pressure = sense.get_pressure()
        pressure = round(pressure,1)
        logger.log("Pressure: ",pressure)

        time.sleep(1)
except KeyboardInterrupt:
    pass
