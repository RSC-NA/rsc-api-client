# ElevatedRoleSyncResult

What a manual sync did, shaped for eyeballing in a terminal or Swagger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**dry_run** | **bool** |  | 
**fetch_mode** | **str** |  | 
**abort_reason** | **str** |  | 
**members_seen** | **int** |  | 
**roles_added** | **int** |  | 
**roles_removed** | **int** |  | 
**errors** | **int** |  | 
**granted** | **List[Dict[str, object]]** |  | 
**revoked** | **List[Dict[str, object]]** |  | 
**unchanged** | **List[Dict[str, object]]** |  | 
**detail** | **Dict[str, object]** |  | 

## Example

```python
from rscapi.models.elevated_role_sync_result import ElevatedRoleSyncResult

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleSyncResult from a JSON string
elevated_role_sync_result_instance = ElevatedRoleSyncResult.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleSyncResult.to_json())

# convert the object into a dict
elevated_role_sync_result_dict = elevated_role_sync_result_instance.to_dict()
# create an instance of ElevatedRoleSyncResult from a dict
elevated_role_sync_result_from_dict = ElevatedRoleSyncResult.from_dict(elevated_role_sync_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


