# PaginatedTransactionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TransactionResponse]**](TransactionResponse.md) |  | 

## Example

```python
from rscapi.models.paginated_transaction_response_list import PaginatedTransactionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTransactionResponseList from a JSON string
paginated_transaction_response_list_instance = PaginatedTransactionResponseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTransactionResponseList.to_json())

# convert the object into a dict
paginated_transaction_response_list_dict = paginated_transaction_response_list_instance.to_dict()
# create an instance of PaginatedTransactionResponseList from a dict
paginated_transaction_response_list_from_dict = PaginatedTransactionResponseList.from_dict(paginated_transaction_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


