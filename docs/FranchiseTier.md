# FranchiseTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_tier import FranchiseTier

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseTier from a JSON string
franchise_tier_instance = FranchiseTier.from_json(json)
# print the JSON string representation of the object
print(FranchiseTier.to_json())

# convert the object into a dict
franchise_tier_dict = franchise_tier_instance.to_dict()
# create an instance of FranchiseTier from a dict
franchise_tier_form_dict = franchise_tier.from_dict(franchise_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


