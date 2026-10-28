# PaginatedMatchResultListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MatchResultList]**](MatchResultList.md) |  | 

## Example

```python
from rscapi.models.paginated_match_result_list_list import PaginatedMatchResultListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMatchResultListList from a JSON string
paginated_match_result_list_list_instance = PaginatedMatchResultListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMatchResultListList.to_json())

# convert the object into a dict
paginated_match_result_list_list_dict = paginated_match_result_list_list_instance.to_dict()
# create an instance of PaginatedMatchResultListList from a dict
paginated_match_result_list_list_from_dict = PaginatedMatchResultListList.from_dict(paginated_match_result_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


