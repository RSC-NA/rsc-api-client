# ElevatedRoleAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**position** | **str** |  | 
**remove** | **bool** |  | 
**executor** | **int** |  | 

## Example

```python
from rscapi.models.elevated_role_add import ElevatedRoleAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleAdd from a JSON string
elevated_role_add_instance = ElevatedRoleAdd.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleAdd.to_json())

# convert the object into a dict
elevated_role_add_dict = elevated_role_add_instance.to_dict()
# create an instance of ElevatedRoleAdd from a dict
elevated_role_add_from_dict = ElevatedRoleAdd.from_dict(elevated_role_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


