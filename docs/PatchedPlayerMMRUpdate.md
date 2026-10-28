# PatchedPlayerMMRUpdate

PUT/PATCH on a pull: its figures and notes, never which tracker it belongs to.  The generic update used PlayerMMRSerializer, whose nested ``tracker_link`` made every PUT, and any PATCH naming it, a 500. Moving a pull between trackers is ``POST /tracker-links/{id}/migrate_pulls/``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_pulled** | **datetime** |  | [optional] 
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

## Example

```python
from rscapi.models.patched_player_mmr_update import PatchedPlayerMMRUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlayerMMRUpdate from a JSON string
patched_player_mmr_update_instance = PatchedPlayerMMRUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedPlayerMMRUpdate.to_json())

# convert the object into a dict
patched_player_mmr_update_dict = patched_player_mmr_update_instance.to_dict()
# create an instance of PatchedPlayerMMRUpdate from a dict
patched_player_mmr_update_from_dict = PatchedPlayerMMRUpdate.from_dict(patched_player_mmr_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


