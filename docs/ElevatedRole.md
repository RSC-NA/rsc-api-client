# ElevatedRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**league** | [**League**](League.md) |  | 
**position** | **str** |  | 
**gm** | **bool** |  | [optional] [readonly] 
**agm** | **bool** |  | [optional] [readonly] 
**arbiter** | **bool** |  | [optional] [readonly] 
**project_role** | **str** |  | 
**franchise_id** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.elevated_role import ElevatedRole

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRole from a JSON string
elevated_role_instance = ElevatedRole.from_json(json)
# print the JSON string representation of the object
print(ElevatedRole.to_json())

# convert the object into a dict
elevated_role_dict = elevated_role_instance.to_dict()
# create an instance of ElevatedRole from a dict
elevated_role_from_dict = ElevatedRole.from_dict(elevated_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


