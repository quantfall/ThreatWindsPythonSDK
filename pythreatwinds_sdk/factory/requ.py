from abc import ABC, abstractmethod
import os, requests

from ..connection.connection import *


class Request(ABC):
    def __init__(self):
        pass
    
    def add_headers(self):
        tw_api_key = os.environ.get("TW_API_KEY", "")
        tw_api_secret = os.environ.get("TW_API_SECRET", "")
        self.headers = {"api-key":tw_api_key,"api-secret":tw_api_secret}

    def add_params(self,params):
        self.params = params

    def add_body(self,body):
        self.body = body

    @abstractmethod
    def operation(self):
        pass
    

class PostRequest(Request):

    def __init__(self):
        self.connect = Connection()
        self.headers = None
        self.body = None
    
    def operation(self):
        """
        Function for execute the request to the endpoint
        """
        response = requests.post(url=self.connect.endpoint, headers=self.headers, json=self.body)
        return response

class GetRequest(Request):

    def __init__(self):
        self.connect = Connection()
        self.headers = None
        self.params = None
    
    def operation(self):
        """
        Function for execute the request to the endpoint
        """

        if self.params == None:
            response = requests.get(url=self.connect.endpoint,headers=self.headers)
        else:
            response = requests.get(url=self.connect.endpoint, headers=self.headers, params=self.params)
        return response