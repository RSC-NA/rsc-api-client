# TransactionPick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**number** | **int** | Pick in the specific tier. | [readonly] 
**round** | **int** | Specific round in the tier. | [readonly] 
**tier** | **str** |  | [readonly] 
**future_pick** | **bool** |  | [readonly] 
**future_season** | **int** |  | [readonly] 
**pick_from** | **str** | Prefix of franchise this pick came from (if any) | [readonly] 
**original_pick** | **str** | Prefix of franchise this pick originally came from (if any) | [readonly] 

## Example

```python
from rscapi.models.transaction_pick import TransactionPick

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPick from a JSON string
transaction_pick_instance = TransactionPick.from_json(json)
# print the JSON string representation of the object
print(TransactionPick.to_json())

# convert the object into a dict
transaction_pick_dict = transaction_pick_instance.to_dict()
# create an instance of TransactionPick from a dict
transaction_pick_from_dict = TransactionPick.from_dict(transaction_pick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


