# LeaguePlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**league** | [**LeaguePlayerLeague**](LeaguePlayerLeague.md) |  | 
**status** | [**LeaguePlayerStatusEnum**](LeaguePlayerStatusEnum.md) |  | [readonly] 
**season** | **int** |  | 
**captain** | **bool** |  | [optional] 
**contract_length** | **int** |  | 
**current_mmr** | **int** |  | [optional] 
**base_mmr** | **int** |  | [optional] 
**team** | [**PlayerTeam**](PlayerTeam.md) |  | 
**last_updated** | **datetime** |  | [readonly] 
**previous_teams** | [**List[PreviousTeam]**](PreviousTeam.md) |  | [readonly] 
**player** | [**LeaguePlayerMember**](LeaguePlayerMember.md) |  | 
**tier** | [**Tier**](Tier.md) |  | 
**sub_status** | [**SubStatusEnum**](SubStatusEnum.md) |  | 
**waiver_period_end_date** | **datetime** |  | 
**signed_date** | **datetime** |  | 

## Example

```python
from rscapi.models.league_player import LeaguePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayer from a JSON string
league_player_instance = LeaguePlayer.from_json(json)
# print the JSON string representation of the object
print(LeaguePlayer.to_json())

# convert the object into a dict
league_player_dict = league_player_instance.to_dict()
# create an instance of LeaguePlayer from a dict
league_player_from_dict = LeaguePlayer.from_dict(league_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


