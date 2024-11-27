import sqlite3
import time
import random
import data_simulation

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

def generate_data():
    get_data = data_simulation.simulate_data()
    N_level = get_data['N_level']
    P_level = get_data['P_level']
    K_level = get_data['K_level']
    M_level = get_data['M_level']
    timestamp = get_data['timestamp']

    return N_level,P_level,K_level,M_level,timestamp

def createTable():
    cursor.execute('CREATE TABLE SoilVal(N_level REAL NOT NULL, P_level REAL NOT NULL, K_Level REAL NOT NULL, M_level NOT NULL, Time REAL)')
    conn.commit()


def insertData(data):
    query = "INSERT INTO SoilVal VALUES(?,?,?,?,?)"

    cursor.execute(query, data)
    conn.commit()

def activate_data_simulation():
    c = 0
    while True:
        
        data = generate_data()
        insertData(data)
        time.sleep(1)
        print(f'Data inserted, index : {c+1}')
        c+=1

    
def get_data():
    cursor.execute('SELECT * FROM SoilVal')
    data = cursor.fetchall()

    return data

get_data()

