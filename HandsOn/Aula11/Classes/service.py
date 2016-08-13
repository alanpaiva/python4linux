#!/usr/bin/python

class Service:
    def __init__(self,id="",client="",product="",
                      request_date="",
                      cancel_date=""):
        self.id = id        
        self.client = client
        self.product = product
        self.request_date = request_date
        self.cancel_date = cancel_date
