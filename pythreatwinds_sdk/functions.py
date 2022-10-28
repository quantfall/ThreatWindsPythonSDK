from dotenv import load_dotenv

from pythreatwinds_sdk.factory.builders import *
from pythreatwinds_sdk.connection.connection import *
from pythreatwinds_sdk.controller.controller import *

#Function to sent a new entity to API of ThreatWinds
def sent_entities(new_entities):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities
    Note that it returns two values: on request
    successful, returns the response and response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as 
    the first value and 0 as the second value
    """

    #Load .env in environment variables
    load_dotenv()

    #Building new instance of request object
    url = "https://api.sandbox.threatwinds.com/api/v1/entities"
    creator = PostCreatorConcret()
    new_request = creator.build_request()
    new_request.add_headers()
    new_request.connect.add_connection(url)
    new_request.add_body(new_entities)
    return (run_request(new_request))


#Function to request entity definitions to the API of ThreatWinds
def get_def_entities():
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/definitions
    Note that it returns two values: on request
    successful, returns a list of entity definitions and response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as 
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    url = "https://api.sandbox.threatwinds.com/api/v1/entities/definitions"
    creator = GetCreatorConcret()
    new_request = creator.build_request()
    new_request.add_headers()
    new_request.connect.add_connection(url)
    return (run_request(new_request))