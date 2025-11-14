import serial
import csv
from datetime import datetime

# update COM3 to your Arduino's port (find it in Arduino IDE under Tools > Port)
ser = serial.Serial('COM3', 9600)

with open('arduino_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Value'])  # Header row
    
    print("Recording... Press Ctrl+C to stop")
    try:
        while True:
            line = ser.readline().decode().strip()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            writer.writerow([timestamp, line])
            print(f"{timestamp}: {line}")  # Shows what's being recorded
    except KeyboardInterrupt:
        print("\nRecording stopped. Data saved to arduino_data.csv")

ser.close()