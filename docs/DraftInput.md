# DraftInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player** | **int** |  | 
**team** | **str** |  | 
**round** | **int** |  | 
**number** | **int** |  | 

## Example

```python
from rscapi.models.draft_input import DraftInput

# TODO update the JSON string below
json = "{}"
# create an instance of DraftInput from a JSON string
draft_input_instance = DraftInput.from_json(json)
# print the JSON string representation of the object
print(DraftInput.to_json())

# convert the object into a dict
draft_input_dict = draft_input_instance.to_dict()
# create an instance of DraftInput from a dict
draft_input_from_dict = DraftInput.from_dict(draft_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


