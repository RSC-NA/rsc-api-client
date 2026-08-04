# WaiverClaimResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**season** | **int** |  | [optional] [readonly] 
**tier** | **int** |  | [optional] [readonly] 
**franchise** | [**TransactionFranchise**](TransactionFranchise.md) |  | 
**team** | [**TransactionTeam**](TransactionTeam.md) |  | 
**player** | [**LeaguePlayer**](LeaguePlayer.md) |  | 
**drop_player** | [**LeaguePlayer**](LeaguePlayer.md) |  | 
**status** | [**WaiverClaimResponseStatusEnum**](WaiverClaimResponseStatusEnum.md) |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.waiver_claim_response import WaiverClaimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WaiverClaimResponse from a JSON string
waiver_claim_response_instance = WaiverClaimResponse.from_json(json)
# print the JSON string representation of the object
print(WaiverClaimResponse.to_json())

# convert the object into a dict
waiver_claim_response_dict = waiver_claim_response_instance.to_dict()
# create an instance of WaiverClaimResponse from a dict
waiver_claim_response_from_dict = WaiverClaimResponse.from_dict(waiver_claim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


