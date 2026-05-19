# LeagueEventDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**league** | **int** |  | [readonly] 
**category** | [**CategoryEnum**](CategoryEnum.md) |  | [readonly] 
**action** | **str** |  | [readonly] 
**actor** | [**LeagueEventActor**](LeagueEventActor.md) |  | [readonly] 
**object_id** | **int** |  | [readonly] 
**payload** | **object** |  | [readonly] 
**is_public** | **bool** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 

## Example

```python
from rscapi.models.league_event_detail import LeagueEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueEventDetail from a JSON string
league_event_detail_instance = LeagueEventDetail.from_json(json)
# print the JSON string representation of the object
print(LeagueEventDetail.to_json())

# convert the object into a dict
league_event_detail_dict = league_event_detail_instance.to_dict()
# create an instance of LeagueEventDetail from a dict
league_event_detail_from_dict = LeagueEventDetail.from_dict(league_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


