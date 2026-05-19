# LeagueEventList


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
from rscapi.models.league_event_list import LeagueEventList

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueEventList from a JSON string
league_event_list_instance = LeagueEventList.from_json(json)
# print the JSON string representation of the object
print(LeagueEventList.to_json())

# convert the object into a dict
league_event_list_dict = league_event_list_instance.to_dict()
# create an instance of LeagueEventList from a dict
league_event_list_from_dict = LeagueEventList.from_dict(league_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


