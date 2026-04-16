# DraftPickGM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**rsc_name** | **str** |  | [optional] 
**discord_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.draft_pick_gm import DraftPickGM

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickGM from a JSON string
draft_pick_gm_instance = DraftPickGM.from_json(json)
# print the JSON string representation of the object
print(DraftPickGM.to_json())

# convert the object into a dict
draft_pick_gm_dict = draft_pick_gm_instance.to_dict()
# create an instance of DraftPickGM from a dict
draft_pick_gm_from_dict = DraftPickGM.from_dict(draft_pick_gm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


