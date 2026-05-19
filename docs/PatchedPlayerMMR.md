# PatchedPlayerMMR


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_pulled** | **datetime** |  | [optional] 
**tracker_link** | [**TrackerMMR**](TrackerMMR.md) |  | [optional] 
**threes_rating** | **int** |  | [optional] 
**threes_season_peak** | **int** |  | [optional] 
**threes_games_played** | **int** |  | [optional] 
**twos_rating** | **int** |  | [optional] 
**twos_season_peak** | **int** |  | [optional] 
**twos_games_played** | **int** |  | [optional] 
**ones_rating** | **int** |  | [optional] 
**ones_season_peak** | **int** |  | [optional] 
**ones_games_played** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**psyonix_season** | **int** |  | [optional] 
**member** | **str** |  | [optional] [readonly] 
**type** | [**PlayerMMRTypeEnum**](PlayerMMRTypeEnum.md) |  | [optional] [readonly] 
**rscid** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_player_mmr import PatchedPlayerMMR

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlayerMMR from a JSON string
patched_player_mmr_instance = PatchedPlayerMMR.from_json(json)
# print the JSON string representation of the object
print(PatchedPlayerMMR.to_json())

# convert the object into a dict
patched_player_mmr_dict = patched_player_mmr_instance.to_dict()
# create an instance of PatchedPlayerMMR from a dict
patched_player_mmr_from_dict = PatchedPlayerMMR.from_dict(patched_player_mmr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


