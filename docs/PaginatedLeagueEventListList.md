# PaginatedLeagueEventListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LeagueEventList]**](LeagueEventList.md) |  | 

## Example

```python
from rscapi.models.paginated_league_event_list_list import PaginatedLeagueEventListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLeagueEventListList from a JSON string
paginated_league_event_list_list_instance = PaginatedLeagueEventListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLeagueEventListList.to_json())

# convert the object into a dict
paginated_league_event_list_list_dict = paginated_league_event_list_list_instance.to_dict()
# create an instance of PaginatedLeagueEventListList from a dict
paginated_league_event_list_list_from_dict = PaginatedLeagueEventListList.from_dict(paginated_league_event_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


