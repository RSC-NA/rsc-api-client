# DraftPickLeaguePlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**discord_id** | **int** |  | 

## Example

```python
from rscapi.models.draft_pick_league_player import DraftPickLeaguePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickLeaguePlayer from a JSON string
draft_pick_league_player_instance = DraftPickLeaguePlayer.from_json(json)
# print the JSON string representation of the object
print(DraftPickLeaguePlayer.to_json())

# convert the object into a dict
draft_pick_league_player_dict = draft_pick_league_player_instance.to_dict()
# create an instance of DraftPickLeaguePlayer from a dict
draft_pick_league_player_from_dict = DraftPickLeaguePlayer.from_dict(draft_pick_league_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


