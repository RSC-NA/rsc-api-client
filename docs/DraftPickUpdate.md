# DraftPickUpdate

PUT/PATCH on a pick: its slot and flags. Owners change through trades and swaps.  The generic update used DraftPickDetailsSerializer, whose nested franchise, tier and players were writable on paper and raised on save (500).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**round** | **int** |  | [optional] 
**future_pick** | **bool** |  | [optional] 
**deleted** | **bool** | Is this pick removed because someone lost a tier. | [optional] 
**future_season** | **int** |  | [optional] 
**pick_from** | **str** | Prefix of franchise this pick came from (if any) | [optional] 
**original_pick** | **str** | Prefix of franchise this pick originally came from (if any) | [optional] 

## Example

```python
from rscapi.models.draft_pick_update import DraftPickUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickUpdate from a JSON string
draft_pick_update_instance = DraftPickUpdate.from_json(json)
# print the JSON string representation of the object
print(DraftPickUpdate.to_json())

# convert the object into a dict
draft_pick_update_dict = draft_pick_update_instance.to_dict()
# create an instance of DraftPickUpdate from a dict
draft_pick_update_from_dict = DraftPickUpdate.from_dict(draft_pick_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


