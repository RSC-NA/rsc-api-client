# FutureSeasonTierOverride

Per-tier replacements for values otherwise copied from the current season.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **int** | Tier id being overridden. | 
**mmr_min** | **int** |  | [optional] 
**mmr_max** | **int** |  | [optional] 
**mmr_promo** | **int** |  | [optional] 
**team_cap** | **int** |  | [optional] 
**team_number** | **int** |  | [optional] 
**transactions_end_date** | **datetime** |  | [optional] 

## Example

```python
from rscapi.models.future_season_tier_override import FutureSeasonTierOverride

# TODO update the JSON string below
json = "{}"
# create an instance of FutureSeasonTierOverride from a JSON string
future_season_tier_override_instance = FutureSeasonTierOverride.from_json(json)
# print the JSON string representation of the object
print(FutureSeasonTierOverride.to_json())

# convert the object into a dict
future_season_tier_override_dict = future_season_tier_override_instance.to_dict()
# create an instance of FutureSeasonTierOverride from a dict
future_season_tier_override_from_dict = FutureSeasonTierOverride.from_dict(future_season_tier_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


