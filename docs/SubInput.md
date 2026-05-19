# SubInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player_in** | **int** |  | 
**player_out** | **int** |  | 

## Example

```python
from rscapi.models.sub_input import SubInput

# TODO update the JSON string below
json = "{}"
# create an instance of SubInput from a JSON string
sub_input_instance = SubInput.from_json(json)
# print the JSON string representation of the object
print(SubInput.to_json())

# convert the object into a dict
sub_input_dict = sub_input_instance.to_dict()
# create an instance of SubInput from a dict
sub_input_from_dict = SubInput.from_dict(sub_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


