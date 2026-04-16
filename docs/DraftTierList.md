# DraftTierList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from rscapi.models.draft_tier_list import DraftTierList

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTierList from a JSON string
draft_tier_list_instance = DraftTierList.from_json(json)
# print the JSON string representation of the object
print(DraftTierList.to_json())

# convert the object into a dict
draft_tier_list_dict = draft_tier_list_instance.to_dict()
# create an instance of DraftTierList from a dict
draft_tier_list_from_dict = DraftTierList.from_dict(draft_tier_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


