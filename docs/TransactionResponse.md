# TransactionResponse

This serializer class will likely be replaced with something more robust later. But for now, we just need to know something is being returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_updates** | [**List[PlayerTransactionUpdates]**](PlayerTransactionUpdates.md) |  | [optional] 
**pick_trades** | [**List[PickTransactionUpdates]**](PickTransactionUpdates.md) |  | [optional] 
**var_date** | **datetime** | Date transaction occurred | [readonly] 
**week** | [**WeekEnum**](WeekEnum.md) |  | 
**week_no** | **int** | Week no of transaction (if applicable) | [optional] 
**match_day** | **int** | Specific match day of the transactions. | [optional] 
**type** | [**TransactionResponseTypeEnum**](TransactionResponseTypeEnum.md) |  | 
**notes** | **str** |  | 
**first_franchise** | [**TransactionFranchise**](TransactionFranchise.md) |  | [optional] 
**second_franchise** | [**TransactionFranchise**](TransactionFranchise.md) |  | [optional] 
**executor** | [**SimpleMember**](SimpleMember.md) |  | 
**id** | **int** |  | [readonly] 

## Example

```python
from rscapi.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionResponse.to_json())

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_from_dict = TransactionResponse.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


