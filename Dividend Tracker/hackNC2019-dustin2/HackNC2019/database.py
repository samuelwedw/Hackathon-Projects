# receives calls of request object builder

# calls request object builder for each request

# receives data from request object builder

# stores data in a dictionary
# dictionary key:
#   symbol
#   exDate
#   paymentDate
#   recordDate
#   declaredDate
#   amount
#   flag
#   currency
#   description
#   frequency
#   date
# from HackNC2019.test import dictionary

# ----------------------------------------------------------------------
# Import Section
# ----------------------------------------------------------------------

import json
import API
import os

# ----------------------------------------------------------------------
# Class Section
# ----------------------------------------------------------------------

class Database:
    def __init__(self, name):
        self.name = name

    def export(self):
        API_CONNECTION = API.API_CONNECTOR("sk_f79736950491411c9a02a29d27108aa0",
                                           "pk_dc0f023c3e8a445c96dd513c6f795060", "https://cloud.iexapis.com/stable/")
        CALL_BACK = API_CONNECTION.check_stock_dividend(self.name)  # placeholder test
        with open('dividend_' + self.name + '.json', 'w') as result:
            json.dump(CALL_BACK, result)
        return CALL_BACK

    def export_quote(self):
        API_CONNECTION = API.API_CONNECTOR("sk_f79736950491411c9a02a29d27108aa0",
                                           "pk_dc0f023c3e8a445c96dd513c6f795060", "https://cloud.iexapis.com/stable/")
        CALL_BACK = API_CONNECTION.check_stock_quote(self.name)  # placeholder test
        with open('quote_' + self.name + '.json', 'w') as result:
            json.dump(CALL_BACK, result)
        return CALL_BACK
    
    def retrieve(self):
        with open('dividend_' + self.name + '.json') as result:
            data = json.load(result)
            return data

    def retrieve_quote(self):
        with open('quote_'+ self.name + '.json') as result:
            data = json.load(result)
            return data

# ----------------------------------------------------------------------
# Function Section
# ----------------------------------------------------------------------


def data_store():
    filename = [file for file in os.listdir()]
    return_dict = {}
    for file in filename:
        if file.endswith('.json') & file.startswith('dividend_'):
            with open(file) as data:
                data = json.load(data)
            data_entry = {file[9:-5]: data}
            return_dict.update(data_entry)
    return return_dict

def data_store_quote():
    filename = [file for file in os.listdir()]
    return_dict = {}
    for file in filename:
        if file.endswith('.json') & file.startswith('quote_'):
            with open(file) as data:
                data = json.load(data)
            data_entry = {file[7:-5]: data}
            return_dict.update(data_entry)
    return return_dict
    

def delete(file):
    if 'dividend_'+ file + '.json' in os.listdir():
        os.remove('dividend_'+ file + '.json')

def delete_quote(file):
    if 'quote_'+ file + '.json' in os.listdir():
        os.remove('quote_'+ file + '.json')


def return_dividends():
    filename = [file for file in os.listdir()]
    return_dict = []
    for file in filename:
        if file.endswith('.json') & file.startswith('dividend_'):
            with open(file) as data:
                data = json.load(data)
            data_entry = {file[9:-5]: data}
            return_dict.append(data_entry)
    return return_dict


# delete("WMT")

""" input_var = "WMT"
create_entry = Database(input_var)
create_stock_input = create_entry.export()
print(create_stock_input)

watchlist = data_store()
print(watchlist) """

# make a remove files function
