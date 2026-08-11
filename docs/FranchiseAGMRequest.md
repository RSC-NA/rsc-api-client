# FranchiseAGMRequest

Body for add_agm / remove_agm.  Both members are addressed by Discord ID, matching FranchiseTransferRequestSerializer: the bot never holds database ids. No `league` field -- the franchise in the path already fixes it, and accepting one would invite a mismatch to arbitrate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agm** | **int** | Discord ID of the member to add or remove. | 
**executor** | **int** | Discord ID of the admin performing this. Must hold Admin in the franchise&#39;s league. | 

## Example

```python
from rscapi.models.franchise_agm_request import FranchiseAGMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FranchiseAGMRequest from a JSON string
franchise_agm_request_instance = FranchiseAGMRequest.from_json(json)
# print the JSON string representation of the object
print(FranchiseAGMRequest.to_json())

# convert the object into a dict
franchise_agm_request_dict = franchise_agm_request_instance.to_dict()
# create an instance of FranchiseAGMRequest from a dict
franchise_agm_request_from_dict = FranchiseAGMRequest.from_dict(franchise_agm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


