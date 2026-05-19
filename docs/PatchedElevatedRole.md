# PatchedElevatedRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**member** | [**SimpleMember**](SimpleMember.md) |  | [optional] [readonly] 
**league** | [**ElevatedRoleLeague**](ElevatedRoleLeague.md) |  | [optional] 
**position** | **str** |  | [optional] 
**gm** | **bool** |  | [optional] [readonly] 
**agm** | **bool** |  | [optional] [readonly] 
**arbiter** | **bool** |  | [optional] [readonly] 
**project_role** | **str** |  | [optional] 
**franchise_id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_elevated_role import PatchedElevatedRole

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedElevatedRole from a JSON string
patched_elevated_role_instance = PatchedElevatedRole.from_json(json)
# print the JSON string representation of the object
print(PatchedElevatedRole.to_json())

# convert the object into a dict
patched_elevated_role_dict = patched_elevated_role_instance.to_dict()
# create an instance of PatchedElevatedRole from a dict
patched_elevated_role_from_dict = PatchedElevatedRole.from_dict(patched_elevated_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


