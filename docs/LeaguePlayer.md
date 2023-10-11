# LeaguePlayer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**league** | [**League**](League.md) |  | 
**status** | **str** |  | [optional] [readonly] 
**season** | **int** |  | 
**captain** | **bool** |  | [optional] [readonly] 
**base_mmr** | **int** |  | [optional] [readonly] 
**current_mmr** | **int** |  | [optional] [readonly] 
**contract_length** | **int** |  | [optional] [readonly] 
**team** | [**PlayerTeam**](PlayerTeam.md) |  | 
**last_updated** | **datetime** |  | [optional] [readonly] 
**previous_teams** | [**List[PreviousTeam]**](PreviousTeam.md) |  | 
**player** | [**LeaguePlayerMember**](LeaguePlayerMember.md) |  | 

## Example

```python
from openapi_client.models.league_player import LeaguePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayer from a JSON string
league_player_instance = LeaguePlayer.from_json(json)
# print the JSON string representation of the object
print LeaguePlayer.to_json()

# convert the object into a dict
league_player_dict = league_player_instance.to_dict()
# create an instance of LeaguePlayer from a dict
league_player_form_dict = league_player.from_dict(league_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


