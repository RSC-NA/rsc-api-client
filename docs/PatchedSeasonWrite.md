# PatchedSeasonWrite

POST/PUT/PATCH on a season: its number and dates.  The generic routes used SeasonSerializer, whose nested ``league`` and ``season_tier_data`` were writable on paper and raised on save (500), while scalar fields were silently ignored. ``league`` is set on create only; ``current`` stays with the rollover, which keeps one current season per league.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | [optional] 
**number** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**preseason_start_date** | **datetime** |  | [optional] 
**regular_season_start** | **datetime** |  | [optional] 
**regular_season_end** | **datetime** |  | [optional] 
**signup_close** | **datetime** |  | [optional] 
**signups_open** | **datetime** |  | [optional] 
**draft_date** | **datetime** |  | [optional] 
**preseason_matches** | **int** |  | [optional] 
**number_of_games** | **int** |  | [optional] 

## Example

```python
from rscapi.models.patched_season_write import PatchedSeasonWrite

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSeasonWrite from a JSON string
patched_season_write_instance = PatchedSeasonWrite.from_json(json)
# print the JSON string representation of the object
print(PatchedSeasonWrite.to_json())

# convert the object into a dict
patched_season_write_dict = patched_season_write_instance.to_dict()
# create an instance of PatchedSeasonWrite from a dict
patched_season_write_from_dict = PatchedSeasonWrite.from_dict(patched_season_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


