import serial
import time

def measure_voltage(npcl_value):
    arduino = serial.Serial('COM3', 9600) # Replace 'COM3' with the appropriate port for your setup
    arduino.write(str(npcl_value).encode()) # send the NPLC value to the Arduino
    time.sleep(1) # wait for 1 second for the Arduino to respond
    voltage = float(arduino.readline().decode().strip()) # read the voltage from the Arduino
    arduino.close()
    return voltage

for i in [1, 5, 10]
    npcl_value = i
    voltage = measure_voltage(npcl_value)
    print("Voltage with NPLC {}: {}".format(npcl_value, voltage))

