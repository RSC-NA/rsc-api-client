# LeaguePlayerLeague


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**guild_id** | **int** |  | 

## Example

```python
from rscapi.models.league_player_league import LeaguePlayerLeague

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayerLeague from a JSON string
league_player_league_instance = LeaguePlayerLeague.from_json(json)
# print the JSON string representation of the object
print LeaguePlayerLeague.to_json()

# convert the object into a dict
league_player_league_dict = league_player_league_instance.to_dict()
# create an instance of LeaguePlayerLeague from a dict
league_player_league_form_dict = league_player_league.from_dict(league_player_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


