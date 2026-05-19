# FranchiseRebrand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | 
**name** | **str** |  | 
**teams** | [**List[TeamRebrand]**](TeamRebrand.md) |  | 
**admin_override** | **bool** |  | 

## Example

```python
from rscapi.models.franchise_rebrand import FranchiseRebrand

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseRebrand from a JSON string
franchise_rebrand_instance = FranchiseRebrand.from_json(json)
# print the JSON string representation of the object
print(FranchiseRebrand.to_json())

# convert the object into a dict
franchise_rebrand_dict = franchise_rebrand_instance.to_dict()
# create an instance of FranchiseRebrand from a dict
franchise_rebrand_from_dict = FranchiseRebrand.from_dict(franchise_rebrand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


