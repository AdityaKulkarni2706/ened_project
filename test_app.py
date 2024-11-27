from flask import Flask, jsonify
import serial

app = Flask(__name__)

SERIAL_PORT = 'COM5'
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Serial port connected.")
except serial.SerialException as e:
    print(f"Error: {e}")
    ser = None

@app.route('/data', methods=['GET'])
def get_data():
    if ser and ser.is_open:
        try:
            # Directly read from the serial port
            data = ser.readline().decode('utf-8').strip()
            return jsonify({"data": data})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Serial port not open."}), 500

if __name__ == '__main__':
    app.run(debug=True)
