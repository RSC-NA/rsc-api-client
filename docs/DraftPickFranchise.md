# DraftPickFranchise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**gm** | [**DraftPickGM**](DraftPickGM.md) |  | 

## Example

```python
from rscapi.models.draft_pick_franchise import DraftPickFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickFranchise from a JSON string
draft_pick_franchise_instance = DraftPickFranchise.from_json(json)
# print the JSON string representation of the object
print(DraftPickFranchise.to_json())

# convert the object into a dict
draft_pick_franchise_dict = draft_pick_franchise_instance.to_dict()
# create an instance of DraftPickFranchise from a dict
draft_pick_franchise_from_dict = DraftPickFranchise.from_dict(draft_pick_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


