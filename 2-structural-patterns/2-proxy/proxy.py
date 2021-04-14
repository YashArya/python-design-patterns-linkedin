#!/usr/bin/env python3 

import time

'''
# Scenario
* Producer - resource intensive object
    * Only a fixed number of Producer objects can exist at a time
* Artist - Proxy; Checks to see if a producer becomes available for a Guest
* Guest
'''

class Producer():
    def produce(self):
        print("Producer is busy working!")

    def meet(self):
        print("Producer is available to meet.")

class Proxy():
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        print("Artist is checking if the Producer is ready")

        if self.occupied == "No":
            # if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            
            # Make the producer meet the guest
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy!")

# Instantiate a proxy
proxy = Proxy()

# Make the proxy: Artist produce until producer is available
proxy.produce()

# Change the state to 'occupied'
proxy.occupied = "Yes"

# Make the producer produce
proxy.produce()