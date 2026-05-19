# PaginatedElevatedRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ElevatedRole]**](ElevatedRole.md) |  | 

## Example

```python
from rscapi.models.paginated_elevated_role_list import PaginatedElevatedRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedElevatedRoleList from a JSON string
paginated_elevated_role_list_instance = PaginatedElevatedRoleList.from_json(json)
# print the JSON string representation of the object
print(PaginatedElevatedRoleList.to_json())

# convert the object into a dict
paginated_elevated_role_list_dict = paginated_elevated_role_list_instance.to_dict()
# create an instance of PaginatedElevatedRoleList from a dict
paginated_elevated_role_list_from_dict = PaginatedElevatedRoleList.from_dict(paginated_elevated_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


