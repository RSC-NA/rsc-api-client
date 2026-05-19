# CutSignInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**cut_player** | **int** |  | 
**sign_player** | **int** |  | 

## Example

```python
from rscapi.models.cut_sign_input import CutSignInput

# TODO update the JSON string below
json = "{}"
# create an instance of CutSignInput from a JSON string
cut_sign_input_instance = CutSignInput.from_json(json)
# print the JSON string representation of the object
print(CutSignInput.to_json())

# convert the object into a dict
cut_sign_input_dict = cut_sign_input_instance.to_dict()
# create an instance of CutSignInput from a dict
cut_sign_input_from_dict = CutSignInput.from_dict(cut_sign_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


