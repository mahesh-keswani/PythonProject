from sklearn.linear_model import LinearRegression
from get_data import get_data_of_stocks
import pandas as pd
from generate_random_data import generate_data

def predict_data(company):
    close,opens,low,high,dates,volume = get_data_of_stocks(company)

    X , Y = convert_to_dataFrame(opens,high,low,close,volume)

    reg = LinearRegression()
    reg = reg.fit(X[['opens','high','low','volume']],Y['close'])

    random_close , random_opens , random_high , random_low , random_volume = generate_data(company)
    test_x , test_y  = convert_to_dataFrame(random_opens,random_high,random_low,random_close,random_volume)
    
    predict = reg.predict(test_x[['opens','high','low','volume']])
    
    return predict

def convert_to_dataFrame(opens,high,low,close,volume):
    df = pd.DataFrame({'opens':opens})
    df['high'] = high
    df['low'] = low
    df['volume'] = volume
    
    df1 = pd.DataFrame({'close':close})

    return df,df1
