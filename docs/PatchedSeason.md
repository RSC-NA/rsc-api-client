# PatchedSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**league** | [**SeasonLeague**](SeasonLeague.md) |  | [optional] 
**number** | **int** |  | [optional] [readonly] 
**season_tier_data** | [**List[SeasonTierData]**](SeasonTierData.md) |  | [optional] 
**current** | **bool** |  | [optional] [readonly] 
**start_date** | **datetime** |  | [optional] [readonly] 
**end_date** | **datetime** |  | [optional] [readonly] 
**preseason_start_date** | **datetime** |  | [optional] [readonly] 
**regular_season_start** | **datetime** |  | [optional] [readonly] 
**regular_season_end** | **datetime** |  | [optional] [readonly] 
**signup_close** | **datetime** |  | [optional] [readonly] 
**signups_open** | **datetime** |  | [optional] [readonly] 
**draft_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_season import PatchedSeason

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSeason from a JSON string
patched_season_instance = PatchedSeason.from_json(json)
# print the JSON string representation of the object
print(PatchedSeason.to_json())

# convert the object into a dict
patched_season_dict = patched_season_instance.to_dict()
# create an instance of PatchedSeason from a dict
patched_season_from_dict = PatchedSeason.from_dict(patched_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


