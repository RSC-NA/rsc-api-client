# SeasonWrite

POST/PUT/PATCH on a season: its number and dates.  The generic routes used SeasonSerializer, whose nested ``league`` and ``season_tier_data`` were writable on paper and raised on save (500), while scalar fields were silently ignored. ``league`` is set on create only; ``current`` stays with the rollover, which keeps one current season per league.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**number** | **int** |  | 
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
from rscapi.models.season_write import SeasonWrite

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonWrite from a JSON string
season_write_instance = SeasonWrite.from_json(json)
# print the JSON string representation of the object
print(SeasonWrite.to_json())

# convert the object into a dict
season_write_dict = season_write_instance.to_dict()
# create an instance of SeasonWrite from a dict
season_write_from_dict = SeasonWrite.from_dict(season_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


