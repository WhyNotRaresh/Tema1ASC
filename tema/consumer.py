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
        self.output_str = "%s bought %s"

    def run(self):
        while len(self.carts) != 0:
            # processing order
            order = self.carts.pop(0)
            # register new cart
            cart_id = self.marketplace.new_cart()

            while len(order) != 0:
                # processing request from order
                request = order.pop(0)

                # handle add type request
                if request["type"] == "add":
                    added_products = 0                           # number of products added to cart
                    while added_products < request["quantity"]:  # try adding until request is met
                        # try adding product
                        if self.marketplace.add_to_cart(cart_id, request["product"]):
                            added_products += 1
                        else:
                            sleep(self.retry_time)               # if fail -> retry after some time

                # handle remove type request
                if request["type"] == "remove":
                    for _ in range(0, request["quantity"]):
                        self.marketplace.remove_from_cart(cart_id, request["product"])

            # finished processing order
            cart_items = self.marketplace.place_order(cart_id)
            for product in cart_items:
                print(self.output_str % (self.name, product))    # printing using the format string
