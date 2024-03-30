# SeasonTierData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | 
**mmr_min** | **int** |  | [optional] [readonly] 
**mmr_max** | **int** |  | [optional] [readonly] 
**team_cap** | **int** |  | [optional] [readonly] 
**team_number** | **int** |  | [optional] [readonly] 
**schedule** | [**SeasonSchedule**](SeasonSchedule.md) |  | [optional] 

## Example

```python
from rscapi.models.season_tier_data import SeasonTierData

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonTierData from a JSON string
season_tier_data_instance = SeasonTierData.from_json(json)
# print the JSON string representation of the object
print(SeasonTierData.to_json())

# convert the object into a dict
season_tier_data_dict = season_tier_data_instance.to_dict()
# create an instance of SeasonTierData from a dict
season_tier_data_form_dict = season_tier_data.from_dict(season_tier_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


