from multiprocessing import Process
from picrawler import Picrawler
from time import sleep
import readchar
import serial
import time

# Initialize the serial port
ser = serial.Serial('/dev/ttyACM0', 115200)

# Initial positions of the servos
positions = [40, 60, 180]
message = '{} {} {}  '.format(positions[0], positions[1], positions[2]).encode('utf-8')
ser.write(message)
# Assuming all start at 90 degrees
sweep_speed = 1
def sweep():
    global ser,positions,sweep_speed
    sleep(25)
    positions = [70, 120, 40]
    message = '{} {} {}  '.format(positions[0], positions[1], positions[2]).encode('utf-8')
    ser.write(message)
    for _ in range(30):#if (positions[1]>=105):
        for positions [1] in range(120, 4, -sweep_speed):
            print("MINUSING")
            message = '{} {} {}  '.format(positions[0], positions[1], positions[2]).encode('utf-8')
            ser.write(message)
            #speed+=3
            #ser.flush()
            print(f'Sent to servos: {message.decode()}')
            time.sleep(0.01)
            #elif (positions[1]<=65):
        time.sleep(1)
        #speed = 1
        for positions [1] in range(5, 121, sweep_speed):
             # Move first servo left
            print("adding")
            message = '{} {} {}  '.format(positions[0], positions[1], positions[2]).encode('utf-8')
            ser.write(message)
            #speed+=3
            #ser.flush()
            print(f'Sent to servos: {message.decode()}')
            time.sleep(0.01)
        # Prepare the message in the format '20 30 10'
        #speed = 1
        time.sleep(0.75)
   
crawler = Picrawler([10,11,12,4,5,6,1,2,3,7,8,9])
speed = 90
p = Process(target=sweep)
p.start()
crawler.do_action('forward',11,speed)
crawler.do_action('turn right',5,speed)
crawler.do_action('forward',9,speed)
p.join()

--
