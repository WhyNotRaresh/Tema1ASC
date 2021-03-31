"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Lock
from queue import Queue, Full, Empty
from typing import Dict, List


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer: int):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """

        # Producer related variables
        self.register_lock = Lock()                     # register lock for thread-safe registering of producers
        self.producers_no = 0                           # number of producers
        self.queue_size = queue_size_per_producer       # max queue size for each producer
        self.producer_queues: Dict[int, Queue] = {}     # queues of all producers

        # Consumer related variables
        self.cart_lock = Lock()                         # cart registration lock
        self.consumers_no = 0                           # number of consumers
        self.consumer_carts: Dict[int, list] = {}       # all carts

    def register_producer(self) -> int:
        """
        Returns an id for the producer that calls this.
        """
        self.register_lock.acquire()                                        # acquiring lock
        producer_id = self.producers_no
        self.producer_queues[producer_id] = Queue(self.queue_size)          # creating new queue for the producer
        self.producers_no += 1                                              # increasing number of producers
        self.register_lock.release()                                        # releasing lock
        return producer_id

    def publish(self, producer_id: int, product) -> bool:
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: int
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        try:
            self.producer_queues[producer_id].put_nowait(product)
        except Full:
            return False
        return True

    def new_cart(self) -> int:
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.cart_lock.acquire()                    # acquire lock
        cart_id = self.consumers_no
        self.consumer_carts[cart_id] = []           # creating new cart for the consumer
        self.consumers_no += 1                      # increasing number of consumers
        self.cart_lock.release()                    # releasing lock
        return cart_id

    def add_to_cart(self, cart_id: int, product) -> bool:
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        cart = self.consumer_carts[cart_id]
        for producer_id in range(0, self.producers_no):
            try:
                queue_head = self.producer_queues[producer_id].get_nowait()
                if queue_head == product:
                    cart.append((queue_head, producer_id))
                    print(cart)
                    return True
                else:
                    while True:
                        try:
                            self.producer_queues[producer_id].put_nowait(queue_head)
                            break
                        except Full:
                            continue
            except Empty:
                continue

        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        pass

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        pass
