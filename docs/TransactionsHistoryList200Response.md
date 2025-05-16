# TransactionsHistoryList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TransactionResponse]**](TransactionResponse.md) |  | 

## Example

```python
from rscapi.models.transactions_history_list200_response import TransactionsHistoryList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsHistoryList200Response from a JSON string
transactions_history_list200_response_instance = TransactionsHistoryList200Response.from_json(json)
# print the JSON string representation of the object
print(TransactionsHistoryList200Response.to_json())

# convert the object into a dict
transactions_history_list200_response_dict = transactions_history_list200_response_instance.to_dict()
# create an instance of TransactionsHistoryList200Response from a dict
transactions_history_list200_response_from_dict = TransactionsHistoryList200Response.from_dict(transactions_history_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


