from abc import ABC, abstractmethod
import os, requests

from ..connection.connection import *


class Request(ABC):
    def __init__(self):
        pass
    
    def add_headers(self, connection):
        """
        Function to add TW_AUTHORIZATION or TW API KEY and TW API SECRET to request object headers
        """
        if connection.tw_authorization != "":
            self.headers = {"Authorization":connection.tw_authorization}
        else:
            self.headers = {"api-key":connection.tw_key,"api-secret":connection.tw_secret}

        if connection.cursor != None:
            self.headers["cursor"] = connection.cursor

    @abstractmethod
    def operation(self):
        pass
    
class PostRequest(Request):

    def __init__(self, resource, connection, body):
        self.body = body
        self.connect = connection
        self.connect.tw_endpoint = self.connect.tw_endpoint + "/" + resource
        self.add_headers(connection)
    
    def operation(self):
        """
        Function for execute the request to the endpoint
        """
        response = requests.post(url=self.connect.tw_endpoint, headers=self.headers, json=self.body)
        return response

class GetRequest(Request):

    def __init__(self, resource, connection, params):
        self.params = params
        self.connect = connection
        self.connect.tw_endpoint = self.connect.tw_endpoint + "/" + resource
        self.add_headers(connection)
        
    def operation(self):
        """
        Function for execute the request to the endpoint
        """

        if self.params == None:
            response = requests.get(url=self.connect.tw_endpoint, headers=self.headers)
        else:
            response = requests.get(url=self.connect.tw_endpoint, headers=self.headers, params=self.params)
        return response