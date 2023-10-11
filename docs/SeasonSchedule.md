# SeasonSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches_per_season** | **int** |  | [optional] [readonly] 
**matches_per_night** | **int** |  | [optional] [readonly] 
**match_nights** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.season_schedule import SeasonSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonSchedule from a JSON string
season_schedule_instance = SeasonSchedule.from_json(json)
# print the JSON string representation of the object
print SeasonSchedule.to_json()

# convert the object into a dict
season_schedule_dict = season_schedule_instance.to_dict()
# create an instance of SeasonSchedule from a dict
season_schedule_form_dict = season_schedule.from_dict(season_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


