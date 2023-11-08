# Season


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | [**SeasonLeague**](SeasonLeague.md) |  | 
**number** | **int** |  | [optional] [readonly] 
**season_tier_data** | [**List[SeasonTierData]**](SeasonTierData.md) |  | 
**current** | **bool** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.season import Season

# TODO update the JSON string below
json = "{}"
# create an instance of Season from a JSON string
season_instance = Season.from_json(json)
# print the JSON string representation of the object
print Season.to_json()

# convert the object into a dict
season_dict = season_instance.to_dict()
# create an instance of Season from a dict
season_form_dict = season.from_dict(season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


