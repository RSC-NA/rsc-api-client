# PaginatedNameChangeHistoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[NameChangeHistory]**](NameChangeHistory.md) |  | 

## Example

```python
from rscapi.models.paginated_name_change_history_list import PaginatedNameChangeHistoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedNameChangeHistoryList from a JSON string
paginated_name_change_history_list_instance = PaginatedNameChangeHistoryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedNameChangeHistoryList.to_json())

# convert the object into a dict
paginated_name_change_history_list_dict = paginated_name_change_history_list_instance.to_dict()
# create an instance of PaginatedNameChangeHistoryList from a dict
paginated_name_change_history_list_from_dict = PaginatedNameChangeHistoryList.from_dict(paginated_name_change_history_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


