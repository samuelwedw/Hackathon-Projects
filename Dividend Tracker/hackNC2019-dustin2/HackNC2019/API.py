#This file is used in the code to interpret and enable interaction with external server libaries and repositories, vital to the function of the main code


# ----------------------------------------------------------------------
# Import Section
# ----------------------------------------------------------------------

import requests
import json


# ----------------------------------------------------------------------
# Class section
# ----------------------------------------------------------------------

class API_CONNECTOR:		#Primary Class In API File- Designed to connect to external repository for the Main Programs Use

    def __init__(self, _API_KEY_secret, _API_KEY_public, _API_DOMAIN):	#The Initializatior used to esthablish the program and its internals 

        self._API_KEY_secret = _API_KEY_secret
        self._API_KEY_public = _API_KEY_public
        self._API_DOMAIN = _API_DOMAIN

    def check_stock_quote(self, symbol):	#Designed to request the stock quotes, and return the result for processing

        print("Called check_stock", symbol, self._API_KEY_public, self._API_KEY_secret)
        connection_URL = self._API_DOMAIN + "stock/" + symbol + "/quote"+ "?token=" + self._API_KEY_secret
        JSON = requests.get(connection_URL)
        print(JSON)
        json_data = json.loads(JSON.text)
        if len(json_data) == 0:
            return "Try Another Stock, This stock is Not Currently Aailable on our Provider"	#return requested data, and end method
        else:
            return json_data	#return requested data, and end method
        	#return requested data, and end method

    def check_stock_dividend(self, symbol):	#Designed to check and return the result for a requested stocks dividend

        # print("Called check_stock_dividend", symbol, self._API_KEY_public, self._API_KEY_secret)	#TESTCODE

        # print(self._API_DOMAIN + "stock/" + symbol + "/dividends"+ "/ytd/" + "?token=" + self._API_KEY_secret)	#TESTCODE
        connection_URL = self._API_DOMAIN + "stock/" + symbol + "/dividends"+ "/ytd/" + "?token=" + self._API_KEY_secret
        JSON = requests.get(connection_URL)
        # print(JSON)	#TEST CODE
        json_data = json.loads(JSON.text)
        if len(json_data) == 0:
            return "Try Another Stock, This stock is Not Currently Aailable on our Provider"	#return requested data, and end method
        else:
            return json_data	#return requested data, and end method
       # return json_data	#return requested data, and end method

    def get_provider_data(self, url):	#returns site data about the requested repository
        callback = requests.get(url)
        if callback.status_code != 200:
            print ("Stock Provider provided no data")
            return False

        if len(callback) == 0:
            return False	#return requested data, and end method
        else:
            return callback	#return requested data, and end method

