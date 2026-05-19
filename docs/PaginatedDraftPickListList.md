# PaginatedDraftPickListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DraftPickList]**](DraftPickList.md) |  | 

## Example

```python
from rscapi.models.paginated_draft_pick_list_list import PaginatedDraftPickListList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDraftPickListList from a JSON string
paginated_draft_pick_list_list_instance = PaginatedDraftPickListList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDraftPickListList.to_json())

# convert the object into a dict
paginated_draft_pick_list_list_dict = paginated_draft_pick_list_list_instance.to_dict()
# create an instance of PaginatedDraftPickListList from a dict
paginated_draft_pick_list_list_from_dict = PaginatedDraftPickListList.from_dict(paginated_draft_pick_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


