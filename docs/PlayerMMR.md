# PlayerMMR


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_pulled** | **datetime** |  | 
**tracker_link** | [**TrackerMMR**](TrackerMMR.md) |  | 
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
**member** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**rscid** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.player_mmr import PlayerMMR

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMMR from a JSON string
player_mmr_instance = PlayerMMR.from_json(json)
# print the JSON string representation of the object
print PlayerMMR.to_json()

# convert the object into a dict
player_mmr_dict = player_mmr_instance.to_dict()
# create an instance of PlayerMMR from a dict
player_mmr_form_dict = player_mmr.from_dict(player_mmr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


