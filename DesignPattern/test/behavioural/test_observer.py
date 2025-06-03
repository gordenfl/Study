import unittest

from Behavioural import Observer

class ObserverTester(unittest.TestCase):
    def build_info(self, id, ibm, apple, google):
        return "Observer ID: %d \nIBM Price: %f\nApple Price: %f\nGoogle Price:%f" % (id, ibm, apple, google)

    def test_observer(self):
        stock_grabber = Observer.StockGrabber() # it's an object of subject
        stock_ob1 = Observer.StockObserver(stock_grabber)
        #stock_ob1 = Observer.StockObserver(stock_grabber)
        
        stock_grabber.setIBMPrice(197.00)
        stock_grabber.setApplePrice(17.00)
        stock_grabber.setGooglePrice(97.00)
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 197.00, 17.00, 97.00))
        
        stock_ob2 = Observer.StockObserver(stock_grabber)
        stock_grabber.setIBMPrice(7.00)
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 7.00, 17.00, 97.00))
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 7.00, 17.00, 97.00))
        stock_grabber.setApplePrice(1.00)
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 7.00, 1.00, 97.00))
        stock_grabber.setGooglePrice(9.00)
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 7.00, 1.00, 9.00))
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 7.00, 1.00, 9.00))
        
        stock_grabber.unregister(stock_ob1)
        stock_grabber.setIBMPrice(999.00)
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 999.00, 1.00, 9.00))
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 7.00, 1.00, 9.00))
        stock_grabber.setApplePrice(999.00)
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 999.00, 999.00, 9.00))
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 7.00, 1.00, 9.00))
        stock_grabber.setGooglePrice(999.00)
        self.assertEqual(stock_ob2.getInfo(), self.build_info(2, 999.00, 999.00, 999.00))
        self.assertEqual(stock_ob1.getInfo(), self.build_info(1, 7.00, 1.00, 9.00))