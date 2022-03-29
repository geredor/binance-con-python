import config
import datetime
from ast import For
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET, tld = 'com')
MINIMOS = []
list_of_tickers = client.get_all_tickers()

for tick in list_of_tickers:
    if (tick['symbol'][-4:] != 'USDT' and tick['symbol'][-4:] != 'BUSD'):
        continue
    # print(tick['symbol'][-4:])
    klines = client.get_historical_klines(tick['symbol'],client.KLINE_INTERVAL_8HOUR,"1 Mar, 2021")
    # print(len(klines))
    if(len(klines) == 0):
        continue
    
    prevClosePrice = klines[0][4]
    for i in range (1,len(klines)-1):
        if (prevClosePrice > klines[i][4]):
            prevClosePrice = klines[i][4]
            timestamp = datetime.datetime.fromtimestamp(int(str(klines[i][0])[:-3]))
    # print(prevClosePrice)
    # print("MINIMO DE "+ tick['symbol'] + " ES "+ str(prevClosePrice)+ " DE LA FECHA "+ timestamp.strftime('%d-%m-%Y %H:%M:%S'))
    
    for tick_2 in list_of_tickers:
        if tick_2['symbol'] == tick['symbol']:
            currentPrice_of_Symbol = float(tick_2['price'])
    if currentPrice_of_Symbol < float(prevClosePrice) + float(prevClosePrice) * 0.05:
        print("ESTE ESTA EN MINIMOS ANUALES --------------> "+ tick['symbol'])
        MINIMOS.append(tick['symbol'])
        
print("*****************************************")
print(MINIMOS)
print(len(MINIMOS))
print("*****************************************")