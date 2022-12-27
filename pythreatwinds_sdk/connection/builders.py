import abc, os

from abc import ABC, abstractmethod
from pythreatwinds_sdk.connection.connection import *

from dotenv import load_dotenv

class AbstractBuilderConnection(ABC):

    def build_connection(self):
        return self.conn

    @abstractmethod
    def with_api_url(self):
        pass

    @abstractmethod
    def with_key(self):
        pass

    @abstractmethod
    def with_secret(self):
        pass

    @abstractmethod
    def with_authorization(self):
        pass

class BuilderConnection(AbstractBuilderConnection):
    def __init__(self):
        self.conn = WebClientService()

    def build_client(self) -> WebClientService:
        conn = self.conn
        return conn

    def with_api_url(self,url):
        """
        Method to add the url attribute to the connection. It returns a boolean, 
        if the attribute was assigned correctly it returns True, if there was an error 
        while assigning the attribute it returns False
        """
        if url == "":
            #Load .env in environment variables
            load_dotenv()
            tw_url = os.environ.get("TW_URL", "")

            if tw_url == "":
                return False
            else:
                self.conn.add_url(tw_url)
                return True
        else:
            self.conn.add_url(url)
            return True

    def with_key(self,key):
        """
        Method to add the key attribute to the connection. It returns a boolean, 
        if the attribute was assigned correctly it returns True, if there was 
        an error while assigning the attribute it returns False
        """
        if key == "":
            #Load .env in environment variables
            load_dotenv()
            tw_key = os.environ.get("TW_API_KEY", "")

            if tw_key == "":
                return False
            else:
                self.conn.add_key(tw_key)
                return True
        else:
            self.conn.add_key(key)
            return True

    def with_secret(self,secret):
        """
        Method to add the secret attribute to the connection. It returns a boolean, 
        if the attribute was assigned correctly it returns True, if there was an error 
        while assigning the attribute it returns False
        """
        if secret == "":
            #Load .env in environment variables
            load_dotenv()
            tw_secret = os.environ.get("TW_API_SECRET", "")

            if tw_secret == "":
                return False
            else:
                self.conn.add_secret(tw_secret)
                return True
        else:
            self.conn.add_secret(secret)
            return True

    def with_authorization(self,authorization):
        """
        Method to add the authorization attribute to the connection. It returns a boolean, 
        if the attribute was assigned correctly it returns True, if there was an error 
        while assigning the attribute it returns False
        """
        if authorization == "":
            #Load .env in environment variables
            load_dotenv()
            tw_authorization = os.environ.get("TW_AUTHORIZATION", "")

            if tw_authorization == "":
                return False
            else:
                self.conn.add_authorization(tw_authorization)
                return True
        else:
            self.conn.add_authorization(authorization)
            return True