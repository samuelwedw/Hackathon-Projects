# stores data in a dictionary
# dictionary key:
#   symbol
#   exDate
#   paymentDate
#   recordDate declaredDate amount flag currency description frequency date


def dictionary(name):
    test_dictionary = {
        "symbol": name,
        "exDate": "10/10/10",
        "paymentDate": "10/10/11",
        "recordDate": "10/10/12",
        "declaredDate": "10/10/13",
        "amount": 3.50,
        "flag": "USA",
        "currency": "USD",
        "description": "STONKS",
        "frequency": "one-time",
        "date": "10/10/09"
    }
    return test_dictionary
