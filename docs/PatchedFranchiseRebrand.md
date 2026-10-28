# PatchedFranchiseRebrand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**teams** | [**List[TeamRebrand]**](TeamRebrand.md) |  | [optional] 
**admin_override** | **bool** |  | [optional] [default to False]

## Example

```python
from rscapi.models.patched_franchise_rebrand import PatchedFranchiseRebrand

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFranchiseRebrand from a JSON string
patched_franchise_rebrand_instance = PatchedFranchiseRebrand.from_json(json)
# print the JSON string representation of the object
print(PatchedFranchiseRebrand.to_json())

# convert the object into a dict
patched_franchise_rebrand_dict = patched_franchise_rebrand_instance.to_dict()
# create an instance of PatchedFranchiseRebrand from a dict
patched_franchise_rebrand_from_dict = PatchedFranchiseRebrand.from_dict(patched_franchise_rebrand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


