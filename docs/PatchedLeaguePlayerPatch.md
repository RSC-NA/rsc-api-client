# PatchedLeaguePlayerPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_mmr** | **int** |  | [optional] 
**current_mmr** | **int** |  | [optional] 
**team_name** | **str** |  | [optional] 
**tier** | **int** |  | [optional] 
**status** | [**LeaguePlayerStatusEnum**](LeaguePlayerStatusEnum.md) |  | [optional] 
**executor** | **int** |  | [optional] 
**waiver_period** | **str** |  | [optional] 
**contract_length** | **int** |  | [optional] 
**captain** | **bool** |  | [optional] 
**sub_status** | [**SubStatusEnum**](SubStatusEnum.md) |  | [optional] 

## Example

```python
from rscapi.models.patched_league_player_patch import PatchedLeaguePlayerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLeaguePlayerPatch from a JSON string
patched_league_player_patch_instance = PatchedLeaguePlayerPatch.from_json(json)
# print the JSON string representation of the object
print(PatchedLeaguePlayerPatch.to_json())

# convert the object into a dict
patched_league_player_patch_dict = patched_league_player_patch_instance.to_dict()
# create an instance of PatchedLeaguePlayerPatch from a dict
patched_league_player_patch_from_dict = PatchedLeaguePlayerPatch.from_dict(patched_league_player_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


