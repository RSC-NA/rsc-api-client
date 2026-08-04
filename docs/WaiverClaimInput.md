# WaiverClaimInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player** | **int** |  | 
**team** | **str** |  | 
**drop_player** | **int** | Player to release if the claiming roster is full when the claim is won. | [optional] 

## Example

```python
from rscapi.models.waiver_claim_input import WaiverClaimInput

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverClaimInput from a JSON string
waiver_claim_input_instance = WaiverClaimInput.from_json(json)
# print the JSON string representation of the object
print(WaiverClaimInput.to_json())

# convert the object into a dict
waiver_claim_input_dict = waiver_claim_input_instance.to_dict()
# create an instance of WaiverClaimInput from a dict
waiver_claim_input_from_dict = WaiverClaimInput.from_dict(waiver_claim_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


