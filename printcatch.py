import serial

# Open the serial port
ser = serial.Serial('/dev/ttyACM0', 9600)
#             
ser.write(b"catch")