# FranchiseFuturesValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**franchise_name** | **str** |  | 
**future_season** | **int** |  | 
**is_valid** | **bool** |  | 
**violations** | **List[str]** |  | 

## Example

```python
from rscapi.models.franchise_futures_validation_response import FranchiseFuturesValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseFuturesValidationResponse from a JSON string
franchise_futures_validation_response_instance = FranchiseFuturesValidationResponse.from_json(json)
# print the JSON string representation of the object
print(FranchiseFuturesValidationResponse.to_json())

# convert the object into a dict
franchise_futures_validation_response_dict = franchise_futures_validation_response_instance.to_dict()
# create an instance of FranchiseFuturesValidationResponse from a dict
franchise_futures_validation_response_from_dict = FranchiseFuturesValidationResponse.from_dict(franchise_futures_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


