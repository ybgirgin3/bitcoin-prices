# !/usr/bin/python3
# -*- coding: utf8 -*-
# Filename: connectionControl2.py

import os
import requests
import datetime

# exceptions
# from requests.exceptions import Timeout
# from requests.exceptions import ReadTimeout
# from urllib3.exceptions import NewConnectionError


def check_internet():
    url = 'https://api.binance.com/api/v1/ping'
    # url = 'http://216.58.192.142'
    timeout=5

    try:
        response = requests.get(url, timeout=timeout)
        print("\033[1;32;40m{} ✓".format(response.status_code))
        error_log("\n{}".format(response.status_code))
        pass

    except Exception as e:
        print("1;31;40m{}".format(e))
        error_log(e)
        print("1;31;40mre-running triarbit.py..")
        os.system("python3 triarbit.py")

# logger func
def error_log(e):
    with open("log/Connection Logs.txt", "a") as f:
        dt = str(datetime.datetime.now())
        error = str(e)
        dt_e = '\n{} ~~ {}'.format(error, dt)
        return f.write(dt_e)

# end file
