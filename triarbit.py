# !/usr/bin/python3
# -*- coding: utf8 -*-
# Filename: triarbit.py
# __author == 'Yusuf Berkay Girgin'

# global modules (built-in)
import json
import time
import requests
import platform as plt

# local modules (self-made)
import terminal_cleaner
import connectionControl

# variables for fee calculation
fee = 0.000750
totalOrderPriceBTC = 0.01

# main loop
# this loop needs to convert json file to the collectable in database
def main():

    while True:
        # network controlling
        connectionControl.check_internet()

        # converting 'requests.model.Response' shaped information to the string
        # btc usd
        start_Get = time.time()

        # main api process
        key     = requests.get("https://api.binance.com/api/v3/ticker/price").text
        end_Get = time.time()
        data    = json.loads(key)

        # lists
        symbol_list = []
        price_list  = []

        for elem in data:
            # list processes
            symbol_list.append(elem['symbol'])
            price_list.append(elem['price'])

        # btc ile ilgili olan verilerin depolandığı listeler
        symbol_BTC  = []
        price_BTC   = []

        # btc verilerinin listelere depolanması için işlme yapan kısım
        for i in symbol_list:
            # btc ile biten coin isimlerini bulan kısım
            if i.endswith('BTC'):
                symbol_BTC.append(i)

                # berkay;
                # symbol_list'in içindeki i indexli olan elemanın indexini bu price_list'teki
                # indexini bulup price_BTC'ye ekledik

                # kerem;
                # price_list içinden symbol_list'in i indexli olan elemanın indexini bulup
                # price_BTC'ye ekledik

                price_BTC.append(price_list[symbol_list.index(i)])

        # coin prices
        # TODO: bu coin price işini dict ile yap daha kısa kod ile
        # coin values storing as a string in here so we need to convert it to int or float
        # for making it usable in processes
        BTCDollar = 0
        BNBDollar = 0
        ETHDollar = 0
        BNBBTC    = 0

        # bu time.sleep kısmını neden koyduğumuzu hatırlamıyorum
        time.sleep(2)

        # Finding specified coin from collected coin data
        start_time = time.time()

        for elem in symbol_list:
            if elem == 'BTCUSDT':
                BTCDollar = float(price_list[symbol_list.index(elem)])

            if elem == 'ETHUSDT':
                ETHDollar = float(price_list[symbol_list.index(elem)])

            if elem == 'BNBUSDT':
                BNBDollar = float(price_list[symbol_list.index(elem)])

            if elem == 'BNBBTC':
                BNBBTC = float(price_list[symbol_list.index(elem)])

        end_time = time.time()

        # if requesting api is takes longer than 5s recontrol if internet connection is okay


        terminal_cleaner.clear_terminal()

        print("#### USD BASED PRICES ####")
        print("\033[1;31;40mBTC to Dollar: %.4f" % (BTCDollar))
        print("\033[1;33;40mETH to Dollar: %.4f" % (ETHDollar))
        print("\033[1;36;40mBNB to Dollar: %.4f" % (BNBDollar))
        print("-------------------------------------------------")
        print("\n")
        print("#### COIN BASED PRICES ####")
        print("\033[1;34;40mBNBBTC: {}".format(BNBBTC))
        print("-------------------------------------------------")
        print("\n")
        print("\033[2;37;40m#### FEE BILLS ####")

        # bu fee hesaplaması bir modül olarak yazılacak ve argümanlı fonksiyona direk olarak gönderilecek
        print("Fee: {}".format((fee * totalOrderPriceBTC) * (BTCDollar * 100) * BNBBTC))


        # api fetching and parsing times printer \033[0;37;40m
        # print("{}--- API fetching : {} seconds ---".format(bad_connection_color ,end_Get - start_Get))
        print("--- API fetching : {} seconds ---".format((end_Get - start_Get)))

        print("\033[0;37;40m--- Parsing      : %.8f seconds ---" % (end_time - start_time))


        print("**********************************")

        # listeleri sıfırlayan kısım
        symbol_list.clear()
        price_list.clear()
        symbol_BTC.clear()
        price_BTC.clear()

if __name__ == '__main__':
    import datetime
    connectionControl.error_log("Program started at {}".format(datetime.datetime.now()))
    main()


# end of file
