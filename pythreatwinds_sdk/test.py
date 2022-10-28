from .functions import *

def sent_entities_test():
    """
    This function tests the operation of the function sent_entities
    """
    print("######################################################################")
    print("################ Test of the function sent_entities ############### ")
    print("######################################################################")

    print("\n")

    entity =[
  {
        "type": "malware",
        "value": "Dridex",
        "reputation": -3,
        "attributes": [],
        "associations": [
            {
                "name": "",
                "comment":"",
                "entity":{
                    "type": "ip",
                    "value": "51.178.161.32",
                    "reputation": -3,
                    "attributes":[],
                    "associations":[]
                }
            }
        ]
    }
]

    print("··············NEW ENTITY················")
    print(entity)

    response, code = sent_entities(entity)

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

    associations ={"associations": ["b97f454d-afad-421b-b157-38cda7d0b612", "3b387967-6242-4b8c-a25c-98c6270d1aa0"],"comment": "Any important comment about the association"}

    print("··············NEW ASSOCIATIONS················")
    print(associations)

    response, code = sent_associations(associations)

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

    response, code = get_def_entities()

    print("Showing response:",response)
    print("Showing return code:",code)