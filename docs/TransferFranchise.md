# TransferFranchise


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_manager** | **int** | General manager to transfer franchise to | 
**league** | **int** | League ID to get player contract status of. | 

## Example

```python
from openapi_client.models.transfer_franchise import TransferFranchise

# TODO update the JSON string below
json = "{}"
# create an instance of TransferFranchise from a JSON string
transfer_franchise_instance = TransferFranchise.from_json(json)
# print the JSON string representation of the object
print TransferFranchise.to_json()

# convert the object into a dict
transfer_franchise_dict = transfer_franchise_instance.to_dict()
# create an instance of TransferFranchise from a dict
transfer_franchise_form_dict = transfer_franchise.from_dict(transfer_franchise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


