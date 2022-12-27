from .functions import *
from pythreatwinds_sdk.connection.builders import *

def sent_entities_test():
    """
    This function tests the operation of the function sent_entities
    """
    print("######################################################################")
    print("################ Test of the function sent_entities ############### ")
    print("######################################################################")

    print("\n")

    entity =[{"type":"domain","value":"host-host-file8.com","reputation":-1,"attributes":[],"associations":[]},{"type":"domain","value":"mark1234.duckdns.org","reputation":-1,"attributes":[],"associations":[]},{"type":"domain","value":"host-file-host6.com","reputation":-1,"attributes":[],"associations":[]},{"type":"domain","value":"clipper.guru","reputation":-1,"attributes":[],"associations":[]}]

    print("··············NEW ENTITY················")
    print(entity)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = sent_entities(entity, myConnection)

        print("Showing response:",response)
        print("Showing return code:",code)

def sent_associations_test():
    """
    This function tests the operation of the function sent_associations
    """
    print("######################################################################")
    print("################ Test of the function sent_associations ############### ")
    print("######################################################################")

    print("\n")

    associations ={"associations": ["ece287a0bea20702259fa39680d8686904c325da5f6965e201d8ea5dfd515767", "5d1aea8f65d4f5c2ee6c9ab31b4a861f27c55fc56218a04b598ca76d08e3addf"]}

    print("··············NEW ASSOCIATIONS················")
    print(associations)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = sent_associations(associations, myConnection)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_def_entities_test():
    """
    This function tests the operation of the function get_def_entities
    """
    print("######################################################################")
    print("################ Test of the function get_def_entities ############### ")
    print("######################################################################")

    print("\n")

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_def_entities(myConnection)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_entities_type_test():
    """
    This function tests the operation of the function get_entities_type
    """
    print("######################################################################")
    print("################ Test of the function get_entities_type ############### ")
    print("######################################################################")


    print("\n")

    
    #cursor = ""
    value = "url"
    print("Value: ",value)
    print("format: list")
    print("limit: 50")
    print("lsa: now-24h")

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_entities_type(myConnection, value= value)

        print("Showing response:",response)
        print("Showing return code:",code) 

def get_entity_associations_test():
    """
    This function tests the operation of the function get_entity_associations
    """
    print("######################################################################")
    print("################ Test of the function get_entity_associations ############### ")
    print("######################################################################")

    print("\n")

    #cursor = ""
    value = "ece287a0bea20702259fa39680d8686904c325da5f6965e201d8ea5dfd515767"
    print("Value: ",value)
    print("limit: 50")

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_entity_associations(myConnection, value= value)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_entity_attributes_test():
    """
    This function tests the operation of the function get_entity_attributes
    """
    print("######################################################################")
    print("################ Test of the function get_entity_attributes ############### ")
    print("######################################################################")

    print("\n")

    #cursor = ""
    value = "ece287a0bea20702259fa39680d8686904c325da5f6965e201d8ea5dfd515767"
    print("Value: ",value)
    print("limit: 50")

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_entity_attributes(myConnection, value= value)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_entity_value_test():
    """
    This function tests the operation of the function get_entity_value
    """
    print("######################################################################")
    print("################ Test of the function get_entity_value ############### ")
    print("######################################################################")

    print("\n")
    value = "clipper.guru"
    type = "domain"
    print("Value: ",value)
    print("Type: ",type)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_entity_value(myConnection, value= value, type=type)

        print("Showing response:",response)
        print("Showing return code:",code)

def sent_geoip_location_test():
    """
    This function tests the operation of the function sent_geoip_location
    """
    print("######################################################################")
    print("################ Test of the function sent_geoip_location ############### ")
    print("######################################################################")

    print("\n")

    location ={
  "accuracyRadius": 100,
  "city": "Canberra",
  "country": "Australia",
  "countryCode": "AU",
  "latitude": 453.334,
  "longitude": -453.334,
  "segment": "1.1.1.0/24"
}

    print("··············NEW LOCATION················")
    print(location)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = sent_geoip_location(myConnection,location)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_geoip_location_test():
    """
    This function tests the operation of the function get_geoip_location
    """
    print("######################################################################")
    print("################ Test of the function get_geoip_location ############### ")
    print("######################################################################")

    print("\n")
    ip = "1.1.1.0"
    print("IP: ",ip)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_geoip_location(myConnection,ip)

        print("Showing response:",response)
        print("Showing return code:",code)

def sent_geoip_organization_test():
    """
    This function tests the operation of the function sent_geoip_organization
    """
    print("######################################################################")
    print("################ Test of the function sent_geoip_organization ############### ")
    print("######################################################################")

    print("\n")

    organization ={
  "asn": 353453,
  "aso": "CloudFlare INC",
  "segment": "1.1.1.0/24"
}

    print("··············NEW ORGANIZATION················")
    print(organization)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = sent_geoip_organization(myConnection,organization)

        print("Showing response:",response)
        print("Showing return code:",code)

def get_geoip_organization_test():
    """
    This function tests the operation of the function get_geoip_organization
    """
    print("######################################################################")
    print("################ Test of the function get_geoip_organization ############### ")
    print("######################################################################")

    print("\n")
    ip = "1.1.1.0"
    print("IP: ",ip)

    web_conn_builder = BuilderConnection()
    web_conn_builder.with_api_url("")
    #asig_auth = web_conn_builder.with_authorization('')
    asig_auth1 = web_conn_builder.with_key("")
    asig_auth2 = web_conn_builder.with_secret("")

    if asig_auth1 == False and asig_auth2 == False:
        print("An error occurred while assigning the authentication parameters")
        exit(1)
    else:
        myConnection = web_conn_builder.build_client()
        response, code = get_geoip_organization(myConnection,ip)

        print("Showing response:",response)
        print("Showing return code:",code)