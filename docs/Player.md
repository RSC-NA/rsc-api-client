# Player


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**status** | **str** |  | 
**captain** | **bool** |  | [optional] [readonly] 
**base_mmr** | **int** |  | [optional] [readonly] 
**current_mmr** | **int** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print Player.to_json()

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_form_dict = player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


