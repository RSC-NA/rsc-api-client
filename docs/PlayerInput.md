# PlayerInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player** | **int** |  | 

## Example

```python
from rscapi.models.player_input import PlayerInput

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerInput from a JSON string
player_input_instance = PlayerInput.from_json(json)
# print the JSON string representation of the object
print(PlayerInput.to_json())

# convert the object into a dict
player_input_dict = player_input_instance.to_dict()
# create an instance of PlayerInput from a dict
player_input_from_dict = PlayerInput.from_dict(player_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


