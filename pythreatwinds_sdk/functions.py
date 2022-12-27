from dotenv import load_dotenv

from pythreatwinds_sdk.factory.builders import *
from pythreatwinds_sdk.connection.connection import *
from pythreatwinds_sdk.controller.controller import *

#Function for sent new entities to API of ThreatWinds
def sent_entities(new_entities, conn):
    """
    This function makes a POST request to the endpoint
    for submit new entities to the ThreatWinds API.
    Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "entities"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, conn, new_entities)
    return (run_request(new_request))

#Function for sent new associations to API of ThreatWinds
def sent_associations(new_associations, conn):
    """
    This function makes a POST request to the endpoint for 
    submit new associations to the ThreatWinds API
    Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "entities/associations"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, conn, new_associations)
    return (run_request(new_request))

#Function for request entity definitions to the API of ThreatWinds
def get_def_entities(conn):
    """
    This function makes a GET request to the endpoint
    for request the entity definitions.
    Note that it returns two values: on request
    successful, returns a list of entity definitions and response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as 
    the first value and 0 as the second value
    """
    
    #Building new instance of request object
    resourc = "entities/definitions"
    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc,conn)
    return (run_request(new_request))

#Function for search entities with a type
def get_entities_type(conn, value, limit = 50, lsa ="now-24h", cursor = None):
    """
    This function makes a GET request to the endpoint
    for search entities with a type.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Defining cursor in connection object
    if cursor != None:
        conn.cursor = cursor

    #Building new instance of request object
    params = {"value": value, "limit":limit, "lsa": lsa}
    resourc = "entities/type"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc,conn, params)
    return (run_request(new_request))

#Function for search entity associations with a ID
def get_entity_associations(conn, value, limit = 50, cursor = None):
    """
    This function makes a GET request to the endpoint
    for search entities associations with a ID.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Defining cursor in connection object
    if cursor != None:
        conn.cursor = cursor

    #Building new instance of request object
    params = {"value": value, "limit":limit}
    resourc = "entity/associations"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, conn, params)
    return (run_request(new_request))

#Function for search entity attributes with a ID
def get_entity_attributes(conn, value, limit = 50, cursor = None):
    """
    This function makes a GET request to the endpoint
    for search entities attributes with a ID.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Defining cursor in connection object
    if cursor != None:
        conn.cursor = cursor

    #Building new instance of request object
    params = {"value": value, "limit":limit}
    resourc = "entity/attributes"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, conn, params)
    return (run_request(new_request))

#Function for search entities with a value
def get_entity_value(conn, value, type):
    """
    This function makes a GET request to the endpoint
    for search entities with a value.
    Note that it returns two values: on request
    successful, it returns a list of entities found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    params = {"value": value, "type":type}
    resourc = "entity/value"

    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, conn, params)
    return (run_request(new_request))

#Function for add or update geolocation segments
def sent_geoip_location(conn, new_location):
    """
    This function makes a POST request to the endpoint
    to add or update geolocation segments. Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "geoip/location"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, conn, new_location)
    return (run_request(new_request))

#Function for search a location with IP address
def get_geoip_location(conn, ip):
    """
    This function makes a GET request to the endpoint
    for search a location with IP address.
    Note that it returns two values: on request
    successful, it returns a ip found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "geoip/location/" + ip
    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, conn)
    return (run_request(new_request))

#Function for add or update segments organization
def sent_geoip_organization(conn,new_organization):
    """
    This function makes a POST request to the endpoint
    to add or update segments organization. Note that it returns two values: on request
    successful, returns the successful response and response code(202).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "geoip/organization"
    creator = PostCreatorConcret()
    new_request = creator.build_request(resourc, conn,  new_organization)
    return (run_request(new_request))

#Function for search a organization with IP address
def get_geoip_organization(conn, ip):
    """
    This function makes a GET request to the endpoint
    for search a organization with IP address.
    Note that it returns two values: on request
    successful, it returns a ip found and a response code(200).
    In case of a bad request, it returns the value None and the error code.
    In case there are problems with the connection, return the error body as
    the first value and 0 as the second value
    """

    #Building new instance of request object
    resourc = "geoip/organization/" + ip
    creator = GetCreatorConcret()
    new_request = creator.build_request(resourc, conn)
    return (run_request(new_request))