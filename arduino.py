import serial
import sqlite3
import functions
import time
import json

def get_data_insert_data_arduino():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    cursor = conn.cursor()
    ser = None
    
    try:
        ser = serial.Serial('COM5', 9600, timeout=1)
        print("Successfully connected to COM5.")
        
        # Read data from Arduino
        while True:
            if ser.in_waiting > 0:  # Check if data is available to read
                try:
                    line = ser.readline().decode('utf-8').rstrip()  # Read a line of data
                    print(f"Raw data from Arduino: {line}")
                    
                    # Parse the JSON data
                    data = json.loads(line)
                    
                    # Extract values
                    N_level = float(data['nitrogen'])
                    P_level = float(data['phosphorus'])
                    K_level = float(data['potassium'])  # Fixed spelling
                    M_level = float(data['nmoisture'])
                    timestamp = time.time()
                    
                    # Create data tuple
                    data_tuple = (N_level, P_level, K_level, M_level, timestamp)
                    print(f"Processed data: {data_tuple}")
                    
                    # Insert into database
                    functions.insertData(data_tuple)
                    
                except json.JSONDecodeError as e:
                    print(f"JSON parsing error: {e}")
                    continue
                except KeyError as e:
                    print(f"Missing key in data: {e}")
                    continue
                except ValueError as e:
                    print(f"Value conversion error: {e}")
                    continue
                
            time.sleep(1)  # Small delay to prevent CPU overuse
            
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
    finally:
        if ser is not None and ser.is_open:
            ser.close()
            print("Serial connection closed.")
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    get_data_insert_data_arduino()