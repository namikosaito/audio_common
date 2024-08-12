#!/usr/bin/env python3
import sys
import rospy
import serial
from std_msgs.msg import Float32MultiArray
import time
import numpy as np
import pyaudio


class Audio(object):
    def __init__(self):
        # audio setting
        p = pyaudio.PyAudio()
        print("audio information")
        for index in range(0, p.get_device_count()):
            print(p.get_device_info_by_index(index))
            
        AUDIO_RATE=44100
        RATE = 50
        p=pyaudio.PyAudio()
        self.CHUNK = AUDIO_RATE // RATE 
        self.stream_1=p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = AUDIO_RATE,
                frames_per_buffer = self.CHUNK,
                input = True,
                output = True, 
                input_device_index = 3 # check!!
                ) 

        self.stream_2=p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = AUDIO_RATE,
                frames_per_buffer = self.CHUNK,
                input = True,
                output = True,
                input_device_index = 11 # check!!
                ) 

        self.sensor_pub = rospy.Publisher('/audio_capture/sensor_data', Float32MultiArray, queue_size=1)

    def get_value(self):
        input_1 = self.stream_1.read(self.CHUNK, exception_on_overflow = False)
        input_2 = self.stream_2.read(self.CHUNK, exception_on_overflow = False)
        self.sensor_data =  [sum(np.frombuffer(input_1, dtype="int16") / 32768), sum(np.frombuffer(input_2, dtype="int16") / 32768)]

        return self.sensor_data


if __name__ == "__main__":
    
    rospy.init_node('audio_common', anonymous=True)

    sensor = Audio()

    r = rospy.Rate(50)
    
    while not rospy.is_shutdown():
        sensor_value = sensor.get_value()
        pub_data = Float32MultiArray(data = sensor_value)
        # print (pub_data)
        sensor.sensor_pub.publish(pub_data)

        r.sleep()


    sensor.shutdown()
