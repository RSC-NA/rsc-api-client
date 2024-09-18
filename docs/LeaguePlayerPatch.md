# LeaguePlayerPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_mmr** | **int** |  | [optional] 
**current_mmr** | **int** |  | [optional] 
**team_name** | **str** |  | [optional] 
**tier** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**executor** | **int** |  | 

## Example

```python
from rscapi.models.league_player_patch import LeaguePlayerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayerPatch from a JSON string
league_player_patch_instance = LeaguePlayerPatch.from_json(json)
# print the JSON string representation of the object
print(LeaguePlayerPatch.to_json())

# convert the object into a dict
league_player_patch_dict = league_player_patch_instance.to_dict()
# create an instance of LeaguePlayerPatch from a dict
league_player_patch_form_dict = league_player_patch.from_dict(league_player_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


