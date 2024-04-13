import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC', 'price': 120.84},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF', 'price': 119.775}
        ]
        """ ------------ Add the assertion below ------------ """
        for i, quote in enumerate(quotes):
            with self.subTest(i=i):
                _, bid_price, ask_price, price = getDataPoint(quote)
                # Ensure the calculated price is correct
                self.assertAlmostEqual(price, (bid_price + ask_price) / 2, places=2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC', 'price': 119.84},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF', 'price': 119.775}
        ]
        
        for i, quote in enumerate(quotes):
            with self.subTest(i=i):
                _, bid_price, ask_price, price = getDataPoint(quote)
                # Ensure the calculated price is correct
                self.assertAlmostEqual(price, (bid_price + ask_price) / 2, places=2)
                # Ensure the bid price is greater than the ask price
               

if __name__ == '__main__':
    unittest.main()
