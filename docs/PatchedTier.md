# PatchedTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**color** | **int** |  | [optional] [readonly] 
**position** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_tier import PatchedTier

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTier from a JSON string
patched_tier_instance = PatchedTier.from_json(json)
# print the JSON string representation of the object
print(PatchedTier.to_json())

# convert the object into a dict
patched_tier_dict = patched_tier_instance.to_dict()
# create an instance of PatchedTier from a dict
patched_tier_from_dict = PatchedTier.from_dict(patched_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


