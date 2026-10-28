# LeaguePlayerCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**team_name** | **str** |  | [optional] 
**status** | [**LeaguePlayerStatusEnum**](LeaguePlayerStatusEnum.md) |  | 
**base_mmr** | **int** |  | 
**current_mmr** | **int** |  | 
**tier** | **int** |  | 
**contract_length** | **int** |  | [optional] [default to 0]
**player** | **int** | Discord ID of the member. | 

## Example

```python
from rscapi.models.league_player_create import LeaguePlayerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayerCreate from a JSON string
league_player_create_instance = LeaguePlayerCreate.from_json(json)
# print the JSON string representation of the object
print(LeaguePlayerCreate.to_json())

# convert the object into a dict
league_player_create_dict = league_player_create_instance.to_dict()
# create an instance of LeaguePlayerCreate from a dict
league_player_create_from_dict = LeaguePlayerCreate.from_dict(league_player_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


