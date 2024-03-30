# IntentToPlay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season** | **int** |  | 
**missing** | **bool** |  | [optional] [default to False]
**returning** | **bool** |  | [optional] 
**player** | [**MemberIntent**](MemberIntent.md) |  | [optional] 

## Example

```python
from rscapi.models.intent_to_play import IntentToPlay

# TODO update the JSON string below
json = "{}"
# create an instance of IntentToPlay from a JSON string
intent_to_play_instance = IntentToPlay.from_json(json)
# print the JSON string representation of the object
print(IntentToPlay.to_json())

# convert the object into a dict
intent_to_play_dict = intent_to_play_instance.to_dict()
# create an instance of IntentToPlay from a dict
intent_to_play_form_dict = intent_to_play.from_dict(intent_to_play_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


