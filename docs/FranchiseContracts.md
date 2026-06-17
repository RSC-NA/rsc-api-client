# FranchiseContracts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**gm** | **str** |  | 
**prefix** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.franchise_contracts import FranchiseContracts

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseContracts from a JSON string
franchise_contracts_instance = FranchiseContracts.from_json(json)
# print the JSON string representation of the object
print(FranchiseContracts.to_json())

# convert the object into a dict
franchise_contracts_dict = franchise_contracts_instance.to_dict()
# create an instance of FranchiseContracts from a dict
franchise_contracts_from_dict = FranchiseContracts.from_dict(franchise_contracts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


