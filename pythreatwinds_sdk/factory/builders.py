from abc import ABC, abstractmethod

from .requ import *

class Creator(ABC):
    
    def build_request(self, resourc, connection, request = None):
        # Call the factory method to create a Product object.
        req = self.factory_method(resourc, connection, request)

        return req

    @abstractmethod
    def factory_method(self):
        pass

class PostCreatorConcret(Creator):

    def factory_method(self,resource, conn, body)->Request:
        return PostRequest(resource, conn, body)

class GetCreatorConcret(Creator):
    def factory_method(self, resource, conn, params)->Request:
        return GetRequest(resource, conn, params)