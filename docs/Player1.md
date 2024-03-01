# Player1

Details of Player being traded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Discord ID of player being traded. | [optional] 
**team** | **str** | Name of the team player is being traded to. | [optional] 

## Example

```python
from rscapi.models.player1 import Player1

# TODO update the JSON string below
json = "{}"
# create an instance of Player1 from a JSON string
player1_instance = Player1.from_json(json)
# print the JSON string representation of the object
print Player1.to_json()

# convert the object into a dict
player1_dict = player1_instance.to_dict()
# create an instance of Player1 from a dict
player1_form_dict = player1.from_dict(player1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


