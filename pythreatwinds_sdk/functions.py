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
    resourc = "entities"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, new_entities)
    print(new_request.connect.endpoint)
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

    resourc = "entities/associations"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc,new_associations)
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
    
    resourc = "entities/definitions"
    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc)
    return (run_request(new_request))

#Function to request through a phrase, a search of entities to the ThreatWinds API
def get_entities_search(value, limit = 50, offset = 0):
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
    resourc = "entities/search"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc,params)
    return (run_request(new_request))

#Function to request through a phrase, a search of entities to the ThreatWinds API
def get_entities_type(value, limit = 50, offset = 0, reputation = "bad", accuracy = 0, lsa ="now-24h"):
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
    resourc = "entities/type"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))

#Function to request through an id, a search of entities to the ThreatWinds API
def get_entity_id(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entity/id
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    resourc = "entity/id"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))

#Function to request through an value, a search of entities to the ThreatWinds API
def get_entity_value(value, limit = 50, offset = 0):
    """
    This function makes a GET request to the endpoint
    https://api.sandbox.threatwinds.com/api/v1/entity/value
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code.
    In case of a bad request, it returns the value None and the response code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """
    #Load .env in environment variables
    load_dotenv()
    
    params = {"value": value, "limit":limit, "offset": offset}
    resourc = "entity/value"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, params)
    return (run_request(new_request))