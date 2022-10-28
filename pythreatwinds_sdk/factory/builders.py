from abc import ABC, abstractmethod

from .requ import *

class Creator(ABC):
    
    def build_request(self):
        # Call the factory method to create a Product object.
        req = self.factory_method()

        return req

    @abstractmethod
    def factory_method(self):
        pass

class PostCreatorConcret(Creator):

    def factory_method(self)->Request:
        return PostRequest()

class GetCreatorConcret(Creator):

    def factory_method(self)->Request:
        return GetRequest()