# TransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_updates** | [**List[PlayerTransactionUpdates]**](PlayerTransactionUpdates.md) |  | [optional] 
**var_date** | **datetime** | Date transaction occurred | [optional] [readonly] 
**week** | **str** |  | 
**week_no** | **int** | Week no of transaction (if applicable) | [optional] 
**match_day** | **int** | Specific match day of the transactions. | [optional] 
**type** | **str** |  | 
**notes** | **str** | Notes associated with the transaction. | 
**first_gm** | [**Member**](Member.md) |  | [optional] 
**second_gm** | [**Member**](Member.md) |  | [optional] 
**executor** | [**Member**](Member.md) |  | 

## Example

```python
from rscapi.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print TransactionResponse.to_json()

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_form_dict = transaction_response.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


