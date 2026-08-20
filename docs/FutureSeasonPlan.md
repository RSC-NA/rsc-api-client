# FutureSeasonPlan

What the endpoint did, or would have done under ``dry_run``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **int** |  | 
**season_id** | **int** |  | 
**season_number** | **int** |  | 
**previous_season_id** | **int** |  | 
**dry_run** | **bool** |  | 
**is_valid** | **bool** |  | 
**created** | **Dict[str, int]** |  | 
**tiers** | [**List[FutureSeasonTierPlan]**](FutureSeasonTierPlan.md) |  | 
**blockers** | **List[str]** |  | 
**warnings** | **List[str]** |  | 

## Example

```python
from rscapi.models.future_season_plan import FutureSeasonPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FutureSeasonPlan from a JSON string
future_season_plan_instance = FutureSeasonPlan.from_json(json)
# print the JSON string representation of the object
print(FutureSeasonPlan.to_json())

# convert the object into a dict
future_season_plan_dict = future_season_plan_instance.to_dict()
# create an instance of FutureSeasonPlan from a dict
future_season_plan_from_dict = FutureSeasonPlan.from_dict(future_season_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


