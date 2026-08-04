# ElevatedRoleSyncInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord_id** | **int** | Discord ID of the member to re-sync against their Discord guild roles. | 
**league** | **int** | Limit the sync to one league. Default: every league with Discord role mappings. | [optional] 
**dry_run** | **bool** | Report what would change without writing anything. | [optional] [default to False]

## Example

```python
from rscapi.models.elevated_role_sync_input import ElevatedRoleSyncInput

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleSyncInput from a JSON string
elevated_role_sync_input_instance = ElevatedRoleSyncInput.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleSyncInput.to_json())

# convert the object into a dict
elevated_role_sync_input_dict = elevated_role_sync_input_instance.to_dict()
# create an instance of ElevatedRoleSyncInput from a dict
elevated_role_sync_input_from_dict = ElevatedRoleSyncInput.from_dict(elevated_role_sync_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


