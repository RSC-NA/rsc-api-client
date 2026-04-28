# LeagueEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**league** | **int** |  | [optional] [readonly] 
**category** | **str** |  | [optional] [readonly] 
**action** | **str** |  | [optional] [readonly] 
**actor** | [**LeagueEventActor**](LeagueEventActor.md) |  | [optional] 
**object_id** | **int** |  | [optional] [readonly] 
**payload** | **object** |  | [optional] [readonly] 
**is_public** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

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


