import json
import random
import datetime

################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    if isinstance(quote, dict):
        timestamp_str = quote['timestamp']
        stock = quote['stock']
        price = quote['price']
        bid_price = quote['top_bid']['price']
        ask_price = quote['top_ask']['price']
    else:
        _, _, _, bid_price_str, ask_price_str = quote.split(',')
        bid_price = float(bid_price_str)
        ask_price = float(ask_price_str)

    # Parsing the timestamp string
    try:
        timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        raise ValueError("Invalid timestamp format")

    # Extracting the price
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Invalid price format")

    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if price_b == 0:
        return None # Avoid zero division error
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

            """ ----------- Update to get the ratio --------------- """
            stock_a, bid_price_a, ask_price_a, price_a = getDataPoint(quotes[0])
            stock_b, bid_price_b, ask_price_b, price_b = getDataPoint(quotes[1])

            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock_a, bid_price_a, ask_price_a, price_a))
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock_b, bid_price_b, ask_price_b, price_b))

            # Calculate the ratio
            ratio = getRatio(price_a, price_b)
            print("Ratio %s" % ratio)
        except Exception as e:
            print("Message: %s" % e)
