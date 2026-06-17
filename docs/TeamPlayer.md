# TeamPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**status** | [**LeaguePlayerStatusEnum**](LeaguePlayerStatusEnum.md) |  | [optional] [readonly] 
**captain** | **bool** |  | [optional] [readonly] 
**base_mmr** | **int** |  | [optional] [readonly] 
**current_mmr** | **int** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**discord_id** | **int** |  | 
**sub_status** | [**SubStatusEnum**](SubStatusEnum.md) |  | [optional] [readonly] 

## Example

```python
from rscapi.models.team_player import TeamPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPlayer from a JSON string
team_player_instance = TeamPlayer.from_json(json)
# print the JSON string representation of the object
print(TeamPlayer.to_json())

# convert the object into a dict
team_player_dict = team_player_instance.to_dict()
# create an instance of TeamPlayer from a dict
team_player_from_dict = TeamPlayer.from_dict(team_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


