# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**status** | [**LeaguePlayerStatusEnum**](LeaguePlayerStatusEnum.md) |  | [readonly] 
**captain** | **bool** |  | [readonly] 
**base_mmr** | **int** |  | [readonly] 
**current_mmr** | **int** |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 
**discord_id** | **int** |  | 
**sub_status** | [**SubStatusEnum**](SubStatusEnum.md) |  | [readonly] 

## Example

```python
from rscapi.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


