# IRInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player** | **int** |  | 
**redshirt** | **bool** |  | [optional] [default to False]
**remove_from_ir** | **bool** |  | 

## Example

```python
from rscapi.models.ir_input import IRInput

# TODO update the JSON string below
json = "{}"
# create an instance of IRInput from a JSON string
ir_input_instance = IRInput.from_json(json)
# print the JSON string representation of the object
print(IRInput.to_json())

# convert the object into a dict
ir_input_dict = ir_input_instance.to_dict()
# create an instance of IRInput from a dict
ir_input_from_dict = IRInput.from_dict(ir_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


