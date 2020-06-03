# ----------------------------------------------------------------------
# Import Section
# ----------------------------------------------------------------------

import API
import database


# ----------------------------------------------------------------------
# TESTER CODE
# ----------------------------------------------------------------------

# import json

##API_CONNECTION = API.API_CONNECTOR("sk_f79736950491411c9a02a29d27108aa0", "pk_dc0f023c3e8a445c96dd513c6f795060", "https://cloud.iexapis.com/stable/")
# drone1 = API.API_CONNECTOR.check_stock_dividend("WMT","sk_f79736950491411c9a02a29d27108aa0","pk_dc0f023c3e8a445c96dd513c6f795060", "https://cloud.iexapis.com/v1/stable/")

##CALL_BACK = API_CONNECTION.check_stock_dividend("WMT")
##print(CALL_BACK)

##CALL_BACK = API_CONNECTION.check_stock_quote("AAPL")
##CALL_BACK = API_CONNECTION.check_stock_quote("AAPL")
##print(CALL_BACK)
##print("Test")

#Sprint = database.Database("DELL")
#SPrint2 = Sprint.export()
#print(SPrint2)

#print(database.return_dividends())

test = database.return_dividends()

#print(test[0])
#for key in test:

for d in test:
    for key in d:
        if type(d[key]) is list:
            for dd in d[key]:
                for kk in dd:
                    if kk == "description":
                        print("%s: %s" % (kk, dd[kk]))
                    if kk == "exDate":
                        print("%s: %s" % (kk, dd[kk]))

                    if kk == "recordDate":
                        print("%s: %s" % (kk, dd[kk]))
                    if kk == "paymentDate":
                        print("%s: %s" % (kk, dd[kk]))
                                        
                                        

def find_by_key(data, target):
    pass

#for key in test[key]:
 #  print (test[[key]]['exDate'])
