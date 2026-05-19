# PaginatedMemberList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Member]**](Member.md) |  | 

## Example

```python
from rscapi.models.paginated_member_list import PaginatedMemberList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMemberList from a JSON string
paginated_member_list_instance = PaginatedMemberList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMemberList.to_json())

# convert the object into a dict
paginated_member_list_dict = paginated_member_list_instance.to_dict()
# create an instance of PaginatedMemberList from a dict
paginated_member_list_from_dict = PaginatedMemberList.from_dict(paginated_member_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


