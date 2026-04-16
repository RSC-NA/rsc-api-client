# DraftPickList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**round** | **int** | Specific round in the tier. | [optional] 
**number** | **int** | Pick in the specific tier. | [optional] 
**gm** | **int** |  | 
**tier** | [**SeasonDraftPickList**](SeasonDraftPickList.md) |  | 

## Example

```python
from rscapi.models.draft_pick_list import DraftPickList

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickList from a JSON string
draft_pick_list_instance = DraftPickList.from_json(json)
# print the JSON string representation of the object
print(DraftPickList.to_json())

# convert the object into a dict
draft_pick_list_dict = draft_pick_list_instance.to_dict()
# create an instance of DraftPickList from a dict
draft_pick_list_from_dict = DraftPickList.from_dict(draft_pick_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


