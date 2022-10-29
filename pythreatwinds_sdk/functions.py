from dotenv import load_dotenv

from pythreatwinds_sdk.factory.builders import *
from pythreatwinds_sdk.connection.connection import *
from pythreatwinds_sdk.controller.controller import *

#Function to sent new entities to API of ThreatWinds
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

#Function to sent new associations to API of ThreatWinds
def sent_associations(new_associations):
    """
    This function makes a POST request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/associations
    Note that it returns two values: on request
    successful, returns the response and response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as 
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()

    url = "https://api.sandbox.threatwinds.com/api/v1/entities/associations"
    creator = PostCreatorConcret()
    new_request = creator.build_request()
    new_request.add_headers()
    new_request.connect.add_connection(url)
    new_request.add_body(new_associations)
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

#Function to request through a phrase, a search of entities to the ThreatWinds API
def get_entity_search(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/search
    Note that it returns two values: on request
    successful, returns a list of entities found and response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    url = "https://api.sandbox.threatwinds.com/api/v1/entities/search"

    creator = GetCreatorConcret()
    new_request = creator.build_request()
    new_request.add_headers()
    new_request.connect.add_connection(url)
    new_request.add_params(params)
    return (run_request(new_request))

#Function to request through a phrase, a search of entities to the ThreatWinds API
def get_entity_type(value, limit = 50, offset = 0, reputation = "bad", accuracy = 0, lsa ="now-24h"):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entities/type
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset, "reputation": reputation, "accuracy": accuracy, "lsa": lsa}
    url = "https://api.sandbox.threatwinds.com/api/v1/entities/type"

    creator = GetCreatorConcret()
    new_request = creator.build_request()
    new_request.add_headers()
    new_request.connect.add_connection(url)
    new_request.add_params(params)
    return (run_request(new_request))