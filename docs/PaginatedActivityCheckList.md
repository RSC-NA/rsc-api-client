# PaginatedActivityCheckList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ActivityCheck]**](ActivityCheck.md) |  | 

## Example

```python
from rscapi.models.paginated_activity_check_list import PaginatedActivityCheckList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedActivityCheckList from a JSON string
paginated_activity_check_list_instance = PaginatedActivityCheckList.from_json(json)
# print the JSON string representation of the object
print(PaginatedActivityCheckList.to_json())

# convert the object into a dict
paginated_activity_check_list_dict = paginated_activity_check_list_instance.to_dict()
# create an instance of PaginatedActivityCheckList from a dict
paginated_activity_check_list_from_dict = PaginatedActivityCheckList.from_dict(paginated_activity_check_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


