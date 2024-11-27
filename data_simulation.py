import random
import time

def simulate_data():

    

    N_level = round(random.uniform(0,100),2)
    P_level = round(random.uniform(0,100),2)
    K_level = round(random.uniform(0,100),2)
    M_level = round(random.uniform(0,50),2)

    data = {
        "N_level" :N_level,
        "P_level" : P_level,
        "K_level" : K_level,
        "M_level" : M_level,
        "timestamp" : time.time()
    }
    
    return data


        
    

