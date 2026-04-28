# PickTransactionUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pick** | [**TransactionPick**](TransactionPick.md) |  | 
**source** | [**TransactionFranchise**](TransactionFranchise.md) |  | 
**destination** | [**TransactionFranchise**](TransactionFranchise.md) |  | 

## Example

```python
from rscapi.models.pick_transaction_updates import PickTransactionUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of PickTransactionUpdates from a JSON string
pick_transaction_updates_instance = PickTransactionUpdates.from_json(json)
# print the JSON string representation of the object
print(PickTransactionUpdates.to_json())

# convert the object into a dict
pick_transaction_updates_dict = pick_transaction_updates_instance.to_dict()
# create an instance of PickTransactionUpdates from a dict
pick_transaction_updates_from_dict = PickTransactionUpdates.from_dict(pick_transaction_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


