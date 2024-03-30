# DraftPick

Draft pick being traded. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** | Tier the pick is in | 
**round** | **int** | Round the pick is in. | 
**number** | **int** | Number of pick in round | 
**future** | **bool** | Is the pick a future pick. | 

## Example

```python
from rscapi.models.draft_pick import DraftPick

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPick from a JSON string
draft_pick_instance = DraftPick.from_json(json)
# print the JSON string representation of the object
print(DraftPick.to_json())

# convert the object into a dict
draft_pick_dict = draft_pick_instance.to_dict()
# create an instance of DraftPick from a dict
draft_pick_form_dict = draft_pick.from_dict(draft_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


