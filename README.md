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

_To request entity definitions, you need to call the following function. If the request is correct, the first value received **response** will be a list of entity definitions:
_
```
response, code = pythreatwinds_sdk.sent_entities(new_entities)
```

### Function get_def_entities

_For new entities, you need to call the following function. If the request is correct, the first value received **response** will be message acknowledged:_

```
response, code = pythreatwinds_sdk.get_def_entities()
```