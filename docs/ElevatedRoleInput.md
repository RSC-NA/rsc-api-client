# ElevatedRoleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**position** | **str** |  | 
**executor** | **int** |  | 
**gm** | **bool** |  | [optional] [default to False]
**agm** | **bool** |  | [optional] [default to False]
**franchise** | **int** |  | [optional] 

## Example

```python
from rscapi.models.elevated_role_input import ElevatedRoleInput

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleInput from a JSON string
elevated_role_input_instance = ElevatedRoleInput.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleInput.to_json())

# convert the object into a dict
elevated_role_input_dict = elevated_role_input_instance.to_dict()
# create an instance of ElevatedRoleInput from a dict
elevated_role_input_from_dict = ElevatedRoleInput.from_dict(elevated_role_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


