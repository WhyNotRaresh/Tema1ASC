"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        super().__init__(name=kwargs["name"])
        self.carts: list = carts
        self.marketplace = marketplace
        self.retry_time = retry_wait_time
        self.cart_id = marketplace.new_cart()

    def run(self):
        while len(self.carts) != 0:
            order = self.carts.pop()

            while len(order) != 0:
                request = order.pop()

                if request["type"] == "add":
                    added_products = 0

                    while added_products < request["quantity"]:
                        if self.marketplace.add_to_cart(self.cart_id,
                                                        request["product"]):
                            added_products += 1
                        else:
                            sleep(self.retry_time)

                if request["type"] == "remove":
                    pass

            self.marketplace.place_order(self.cart_id)
