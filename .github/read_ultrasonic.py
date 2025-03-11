import serial
import time

# Initialize the serial connection
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)

try:
    while True:
        if arduino.in_waiting > 0:  # Check if data is available
            distance = arduino.readline().decode('utf-8').strip()
            print(f"Distance: {distance} cm")
        time.sleep(2)
except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()