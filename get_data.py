import requests

def get_data_of_stocks(company):
    close = []
    dates = []
    opens = []
    high = []
    low = []
    volume = []

    if company == "Microsoft":
        key = "MSFT"
    elif company == "Google":
        key = "GOOGL"
    else:
        key = "AAPL"
        
    query_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+key+"&apikey=RC90TGA5BKPHHRVT"

    response = requests.get(query_url)
    data = response.json()

    for i in data["Time Series (Daily)"]:
        close.append(float(data["Time Series (Daily)"][i]["4. close"]))
        opens.append(float(data["Time Series (Daily)"][i]["1. open"]))
        high.append(float(data["Time Series (Daily)"][i]["2. high"]))
        low.append(float(data["Time Series (Daily)"][i]["3. low"]))
        volume.append(float(data["Time Series (Daily)"][i]["6. volume"]))
        dates.append(i)

    return close,opens,low,high,dates,volume
