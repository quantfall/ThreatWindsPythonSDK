# ThreatWindsPythonSDK

_ThreatWindsPythonSDK is a set of tools that allow interaction with ThreatWinds API. This SDK has functions to obtain information about active threats, and at the same time add new threats_

## Getting started
_To work with this SDK you need an AUTHORIZATION, or a KEY and a SECRET. Having this you can pass it to the function as arguments. You can also create in the root of your project an .env file that will contain the values ​​TW_AUTHORIZATION, or TW_API_KEY and TW_API_SECRET with their values._

### Requirements

Python 3.7+
requests 2.28.1
python-dotenv 0.21.0

_For install the requirements:_

```
pip install -r requirements.txt

```

_or:_

```
python -m pip install requests
python -m pip install python-dotenv
```

## Deploy

_First you must create an object of type BuilderConnection, to create the connection as shown below:_

```
conn_builder = BuilderConnection()
```

_Then you must assign the connection attributes, note that these methods return a boolean value, which is True if you have assigned the value without problems and False if an error occurred. To assign the api url attribute, you need to assign it as follows:_

```
conn_builder.with_api_url("https://xxx.threatwinds.xxx")
```

_Depending on the authentication parameters that you are going to use, you must create the connection attributes, if you have the value TW_AUTHORIZACION, you must assign it as follows:_

```
conn_builder.with_authorization('Bearer XXxxxxXxxxxxXXXxXXx')
```

_If you have the value TW_API_KEY and the TW_API_SECRET, you must assign them as follows:_

```
conn_builder.with_key("XXxXXXXXxXXxxxxxxXXxXxX")
conn_builder.with_secret("XXxXXXXXxXXxxxxxxXXxXxX")
```

_If you want to assign these values ​​from environment variables, through the .env file in the root of your project, you can leave the parameters that you pass to the methods empty, as follows:_

```
conn_builder.with_api_url("")
conn_builder.with_authorization("")
conn_builder.with_key("")
conn_builder.with_secret("")
```

_When you assign the connection attributes, you just have to build your connection like this:_

```
my_connection = conn_builder.build_client()
```

_Then you only have to call the function you want to use, and pass the connection created. You should be aware that these functions return two values. The first **response** value will save the response if the request was successful. If it was not successful, it will be the value None. The second value **code**, will be the response code received. In case there is a connection problem, this second value will be 0_

### Function sent_entities

_For insert new entities, you need to call the following function. If the request is correct, the first value received **response** will be an acknowledged message:_

```
response, code = pythreatwinds_sdk.sent_entities(new_entities, my_connection)
```

### Function sent_associations

_For insert new associations, you need to call the following function. If the request is correct, the first value received **response** will be an acknowledged message:_

```
response, code = pythreatwinds_sdk.sent_associations(new_associations, my_connection)
```

### Function get_def_entities

_For request entity definitions, you need to call the following function. If the request is correct, the first value received **response** will be a list of entity definitions:_

```
response, code = pythreatwinds_sdk.get_def_entities(my_connection)
```

### Function get_entities_type

_For find a list of entities of some type, you must call the following function. If the request is correct, the first value received **response** will be a list of the entities found:_
```
response, code = pythreatwinds_sdk.get_entities_type(my_connection, value, limit, lsa, cursor)
```

_Must be passed as arguments:_
    -value: entity type.Must be a string. Consult **Function get_def_entities**
    -limit: Must be an integer>0. Default 50. Is optional
    -lsa: Must be a timestamp in seconds since Unix(UTC) or a relative time like now-15m, now-30m, now-1h, now-8h, now-24h, now-7d, now-30d, now-90d or now-120d. Default now-24h. Is optional
    -cursor: Empty in the first request, then the returned string in the response header  with name: next-cursor

### Function get_entity_associations

_For find an entity associations with an id, you must call to the following function. If the request is correct, the first value received **response** will be the entity found:_
```
response, code = pythreatwinds_sdk.get_entity_associations(my_connection, value, limit, cursor)
```

_Must be passed as arguments:_
    -value: Entity ID. Must be a string
    -limit: Must be an integer>0. Default 50. Is optional
    -cursor: Empty in the first request, then the returned string in the response header  with name: next-cursor

### Function get_entity_attributes

_For find an entity attributes with an id, you must call to the following function. If the request is correct, the first value received **response** will be the entity found:_
```
response, code = pythreatwinds_sdk.get_entity_attributes(my_connection, value, limit, cursor)
```

_Must be passed as arguments:_
    -value: Entity ID. Must be a string
    -limit: Must be an integer>0. Default 50. Is optional
    -cursor: Empty in the first request, then the returned string in the response header  with name: next-cursor

### Function get_entity_value

_For find an entity with an value, you must call to the following function. If the request is correct, the first value received **response** will be the entity found:_
```
response, code = pythreatwinds_sdk.get_entity_value(my_connection, value, type)
```

_Must be passed as arguments:_
    -value: Entity value. Must be a string
    -type: Entity type. Must be a string

### Function sent_geoip_location

_For sent a new location, you need to call the following function. If the request is correct, the first value received **response** will be message acknowledged:_

```
response, code = pythreatwinds_sdk.sent_geoip_location(my_connection,new_location)
```

Where new_location must be an object with the following format:

```
{
  "accuracyRadius": 100,
  "city": "Canberra",
  "country": "Australia",
  "countryCode": "AU",
  "latitude": 453.334,
  "longitude": -453.334,
  "segment": "1.1.1.0/24"
}
```

### Function get_geoip_location

_For find the geolocation of the given IP, you must call to the following function. If the request is correct, the first value received **response** will be the geolocation found:_
```
response, code = pythreatwinds_sdk.get_geoip_location(my_connection,ip)
```

_Must be passed as arguments:_
    -ip: IP address. Must be a string

### Function sent_geoip_organization

_For sent a new organization, you need to call the following function. If the request is correct, the first value received **response** will be message acknowledged:_

```
response, code = pythreatwinds_sdk.sent_geoip_organization(my_connection,new_organization)
```

Where new_location must be an object with the following format:

```
{
  "asn": 353453,
  "aso": "CloudFlare INC",
  "segment": "1.1.1.0/24"
}
```

### Function get_geoip_organization

_For find the organization of the given IP, you must call to the following function. If the request is correct, the first value received **response** will be the organization found:_
```
response, code = pythreatwinds_sdk.get_geoip_organization(my_connection,ip)
```

_Must be passed as arguments:_
    -ip: IP address. Must be a string

## Running tests
If you want to get a demo of how functions work, some test functions with default values ​​have been developed, which you can call by simply adding the phrase _test to the name of the function you want to test. The following example shows how to call the function to test sent_entities:

```
sent_entities_test()
```

## Licence
_This project is under MIT Licence_