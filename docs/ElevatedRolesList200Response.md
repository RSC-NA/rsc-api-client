# ElevatedRolesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ElevatedRole]**](ElevatedRole.md) |  | 

## Example

```python
from rscapi.models.elevated_roles_list200_response import ElevatedRolesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRolesList200Response from a JSON string
elevated_roles_list200_response_instance = ElevatedRolesList200Response.from_json(json)
# print the JSON string representation of the object
print(ElevatedRolesList200Response.to_json())

# convert the object into a dict
elevated_roles_list200_response_dict = elevated_roles_list200_response_instance.to_dict()
# create an instance of ElevatedRolesList200Response from a dict
elevated_roles_list200_response_from_dict = ElevatedRolesList200Response.from_dict(elevated_roles_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


