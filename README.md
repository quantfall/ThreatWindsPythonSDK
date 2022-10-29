# ThreatWindsPythonSDK

_ThreatWindsPythonSDK is a set of tools that allow interaction with ThreatWinds API. This SDK has functions to obtain information about active threats, and at the same time add new threats_

## Getting started
### Requirements

Python 3.7+
requests 2.28.1
python-dotenv 0.21.0

## Deploy

_You should be aware that these functions return two values. The first **response** value will save the response if the request was successful. If it was not successful, it will be the value None. The second value **code**, will be the response code received. In case there is a connection problem, this second value will be 0_

### Function sent_entities

_For new entities, you need to call the following function. If the request is correct, the first value received **response** will be message acknowledged:_

```
response, code = pythreatwinds_sdk.sent_entities(new_entities)
```

Where new_entities must have the following format:

```
[
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
```

### Function sent_associations

_For new associations, you need to call the following function. If the request is correct, the first value received **response** will be message acknowledged:_

```
response, code = pythreatwinds_sdk.sent_associations(new_associations)
```

Where new_associations must have the following format:

```
{
  "associations": [
    "b97f454d-afad-421b-b157-38cda7d0b612", 
    "22721539-0471-440b-829e-069a9cdcc6ae"
  ],
  "comment": "Any important comment about the association"
}
```

### Function get_def_entities

_To request entity definitions, you need to call the following function. If the request is correct, the first value received **response** will be a list of entity definitions:_

```
response, code = pythreatwinds_sdk.get_def_entities()
```

### Function get_entity_search

_To find a list of enttiies containing a string, you must call to the following function:_
```
values, code = pythreatwinds_sdk.get_entity_search(value, limit, offset)
```

_Must be passed as arguments:_
    -value: Must be a string that will be searched.If you don't have quotes, it will be searched as independent words, only elements that contain all the words will be returned. The order of the words doesn't matter. If it is enclosed in quotes: it will be searched as a complete phrase, only elements that contain all the words in the exact order will be returned. The word "or" works like the OR operator in a programming language. The words or, and, the, he, she, it, etc. are not taken into account as search parameters. A hyphen works like the negation operator in a programming language.
    -limit: Must be an integer>0. Default 50. Is optional
    -offset: Must be an integer>=0. Default 0. Is optional