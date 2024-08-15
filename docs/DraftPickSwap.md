# DraftPickSwap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_gm** | **int** |  | 
**to_gm** | **int** |  | 
**round** | **int** |  | 
**tier** | **str** |  | 
**league** | **int** |  | [optional] 
**season** | **int** | Season **number**. | 

## Example

```python
from rscapi.models.draft_pick_swap import DraftPickSwap

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickSwap from a JSON string
draft_pick_swap_instance = DraftPickSwap.from_json(json)
# print the JSON string representation of the object
print(DraftPickSwap.to_json())

# convert the object into a dict
draft_pick_swap_dict = draft_pick_swap_instance.to_dict()
# create an instance of DraftPickSwap from a dict
draft_pick_swap_form_dict = draft_pick_swap.from_dict(draft_pick_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


