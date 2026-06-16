# FranchiseFuturesValidation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**franchise_name** | **str** |  | 

## Example

```python
from rscapi.models.franchise_futures_validation import FranchiseFuturesValidation

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseFuturesValidation from a JSON string
franchise_futures_validation_instance = FranchiseFuturesValidation.from_json(json)
# print the JSON string representation of the object
print(FranchiseFuturesValidation.to_json())

# convert the object into a dict
franchise_futures_validation_dict = franchise_futures_validation_instance.to_dict()
# create an instance of FranchiseFuturesValidation from a dict
franchise_futures_validation_from_dict = FranchiseFuturesValidation.from_dict(franchise_futures_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


