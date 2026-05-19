# Season


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**league** | [**SeasonLeague**](SeasonLeague.md) |  | 
**number** | **int** |  | [readonly] 
**season_tier_data** | [**List[SeasonTierData]**](SeasonTierData.md) |  | 
**current** | **bool** |  | [readonly] 
**start_date** | **datetime** |  | [readonly] 
**end_date** | **datetime** |  | [readonly] 
**preseason_start_date** | **datetime** |  | [readonly] 
**regular_season_start** | **datetime** |  | [readonly] 
**regular_season_end** | **datetime** |  | [readonly] 
**signup_close** | **datetime** |  | [readonly] 
**signups_open** | **datetime** |  | [readonly] 
**draft_date** | **datetime** |  | [readonly] 

## Example

```python
from rscapi.models.season import Season

# TODO update the JSON string below
json = "{}"
# create an instance of Season from a JSON string
season_instance = Season.from_json(json)
# print the JSON string representation of the object
print(Season.to_json())

# convert the object into a dict
season_dict = season_instance.to_dict()
# create an instance of Season from a dict
season_from_dict = Season.from_dict(season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


