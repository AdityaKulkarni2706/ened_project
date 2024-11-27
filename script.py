import serial
import requests
import time


arduino = serial.Serial('COM5', 9600)  # Adjust to your Arduino's serial port
server_url = 'http://127.0.0.1:5000/api/data'  # Flask server URL

while True:
    # Read data from Arduino (assuming data is sent in the format "NPK: 10, 20, 30")
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()  # Read the line and remove extra spaces/newlines
        print(f"Received data: {data}")
        
        try:
            # Parse the data (you may need to adjust the parsing based on your Arduino output)
            # Assuming the format is "NPK: 10, 20, 30" where values are separated by commas
            parts = data.split(":")[1].strip().split(',')
            nitrogen = int(parts[0])
            phosphorus = int(parts[1])
            potassium = int(parts[2])

            # Create the payload to send to the Flask server
            payload = {
                'nitrogen': nitrogen,
                'phosphorus': phosphorus,
                'potassium': potassium
            }

            # Send the data as a POST request to the Flask server
            response = requests.post(server_url, json=payload)

            # Check if the request was successful
            if response.status_code == 200:
                print("Data sent successfully!")
            else:
                print(f"Failed to send data: {response.status_code}")
            
        except ValueError:
            print("Failed to parse the received data.")
        
    time.sleep(1)  # Delay between reading the Arduino data
