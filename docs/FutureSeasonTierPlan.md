# FutureSeasonTierPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **int** |  | 
**tier_name** | **str** |  | 
**franchises** | **int** |  | 
**picks** | **int** |  | 
**num_rounds** | **int** |  | 
**mmr_min** | **int** |  | 
**mmr_max** | **int** |  | 
**mmr_promo** | **int** |  | 
**team_cap** | **int** |  | 
**team_number** | **int** |  | 
**transactions_end_date** | **datetime** |  | 
**schedule_cloned** | **bool** |  | 

## Example

```python
from rscapi.models.future_season_tier_plan import FutureSeasonTierPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FutureSeasonTierPlan from a JSON string
future_season_tier_plan_instance = FutureSeasonTierPlan.from_json(json)
# print the JSON string representation of the object
print(FutureSeasonTierPlan.to_json())

# convert the object into a dict
future_season_tier_plan_dict = future_season_tier_plan_instance.to_dict()
# create an instance of FutureSeasonTierPlan from a dict
future_season_tier_plan_from_dict = FutureSeasonTierPlan.from_dict(future_season_tier_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


