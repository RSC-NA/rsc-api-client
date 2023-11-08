# IntentToPlaySchema

Request body object containing intent to play data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**players** | **List[int]** | List of players to fill out intent for. | 
**league** | **int** | League players are returning to. | 

## Example

```python
from rscapi.models.intent_to_play_schema import IntentToPlaySchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntentToPlaySchema from a JSON string
intent_to_play_schema_instance = IntentToPlaySchema.from_json(json)
# print the JSON string representation of the object
print IntentToPlaySchema.to_json()

# convert the object into a dict
intent_to_play_schema_dict = intent_to_play_schema_instance.to_dict()
# create an instance of IntentToPlaySchema from a dict
intent_to_play_schema_form_dict = intent_to_play_schema.from_dict(intent_to_play_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


