# ElevatedRoleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**position** | [**PositionEnum**](PositionEnum.md) | Staff position. Omit or send null for a gm/agm row, which carries no position.  * &#x60;ADM&#x60; - Admin * &#x60;DEV&#x60; - Development * &#x60;EVENTS&#x60; - Events * &#x60;FRAN&#x60; - Franchise Manager * &#x60;MEDIA&#x60; - Media * &#x60;MMR&#x60; - MMR Puller * &#x60;NH&#x60; - Numbers Head * &#x60;NUMS&#x60; - Numbers * &#x60;STAFF&#x60; - Staff * &#x60;STATS&#x60; - Stats * &#x60;TM&#x60; - Transactions * &#x60;TMH&#x60; - Transactions Head | [optional] 
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


