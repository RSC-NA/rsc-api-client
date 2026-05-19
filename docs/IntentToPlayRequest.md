# IntentToPlayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returning** | **bool** |  | 
**league** | **int** |  | 
**admin_override** | **bool** |  | [optional] 
**executor** | **int** |  | [optional] 

## Example

```python
from rscapi.models.intent_to_play_request import IntentToPlayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntentToPlayRequest from a JSON string
intent_to_play_request_instance = IntentToPlayRequest.from_json(json)
# print the JSON string representation of the object
print(IntentToPlayRequest.to_json())

# convert the object into a dict
intent_to_play_request_dict = intent_to_play_request_instance.to_dict()
# create an instance of IntentToPlayRequest from a dict
intent_to_play_request_from_dict = IntentToPlayRequest.from_dict(intent_to_play_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


