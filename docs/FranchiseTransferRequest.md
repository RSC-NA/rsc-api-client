# FranchiseTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_manager** | **int** |  | 
**league** | **int** |  | 

## Example

```python
from rscapi.models.franchise_transfer_request import FranchiseTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseTransferRequest from a JSON string
franchise_transfer_request_instance = FranchiseTransferRequest.from_json(json)
# print the JSON string representation of the object
print(FranchiseTransferRequest.to_json())

# convert the object into a dict
franchise_transfer_request_dict = franchise_transfer_request_instance.to_dict()
# create an instance of FranchiseTransferRequest from a dict
franchise_transfer_request_from_dict = FranchiseTransferRequest.from_dict(franchise_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


