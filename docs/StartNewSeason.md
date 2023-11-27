# StartNewSeason

Endpoint to start new season for a given league

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Season start date | 
**end_date** | **str** | Season end date | 
**regular_season_start** | **str** | When Regular season starts | 
**signups_close** | **str** | When signups close. | 
**preseason_start_date** | **str** | When the preseason starts | 
**draft_date** | **str** | Planned draft night | 

## Example

```python
from rscapi.models.start_new_season import StartNewSeason

# TODO update the JSON string below
json = "{}"
# create an instance of StartNewSeason from a JSON string
start_new_season_instance = StartNewSeason.from_json(json)
# print the JSON string representation of the object
print StartNewSeason.to_json()

# convert the object into a dict
start_new_season_dict = start_new_season_instance.to_dict()
# create an instance of StartNewSeason from a dict
start_new_season_form_dict = start_new_season.from_dict(start_new_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


