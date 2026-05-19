# PaginatedMatchListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MatchList]**](MatchList.md) |  | 

## Example

```python
from rscapi.models.paginated_match_list_list import PaginatedMatchListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMatchListList from a JSON string
paginated_match_list_list_instance = PaginatedMatchListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMatchListList.to_json())

# convert the object into a dict
paginated_match_list_list_dict = paginated_match_list_list_instance.to_dict()
# create an instance of PaginatedMatchListList from a dict
paginated_match_list_list_from_dict = PaginatedMatchListList.from_dict(paginated_match_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


