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