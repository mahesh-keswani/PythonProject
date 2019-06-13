from get_data import get_data_of_stocks
import numpy as np

def generate_data(company):
    close , opens , low , high , dates , volume = get_data_of_stocks(company)

    random_close = np.random.randint(low = min(close) , high = max(close) , size=30)
    random_opens = np.random.randint(low = min(opens) , high = max(opens) , size=30)
    random_high = np.random.randint(low = min(high) , high = max(high) , size=30)
    random_low = np.random.randint(low = min(low) , high = max(low) , size=30)
    random_volume = np.random.randint(low = min(volume) , high = max(volume) , size=30)
    
    return random_close , random_opens , random_high , random_low , random_volume
                                                                     
