"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        super().__init__(name=kwargs["name"], daemon=kwargs["daemon"])
        self.products = products
        self.marketplace = marketplace
        self.republish_time = republish_wait_time
        self.producer_id = marketplace.register_producer()

    def run(self):
        while True:
            for product in self.products:                   # cycle through products
                produced = 0                                # number of produced items
                waited = False                              # should you wait for production?

                while produced < product[1]:                # produce specific number of products
                    if not waited:
                        sleep(product[2])                   # ... producing ...

                    # trying to publish product for sale
                    if self.marketplace.publish(self.producer_id, product[0]):
                        produced += 1
                        waited = False
                    else:
                        sleep(self.republish_time)          # ... taking a break ...
                        waited = True
