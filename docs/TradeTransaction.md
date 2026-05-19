# TradeTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trades** | [**List[TradeObject]**](TradeObject.md) |  | 
**admin_override** | **bool** |  | [optional] 
**confirm_imbalanced** | **bool** |  | [optional] 
**executor** | **int** |  | 
**notes** | **str** |  | 
**league** | **int** |  | 

## Example

```python
from rscapi.models.trade_transaction import TradeTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TradeTransaction from a JSON string
trade_transaction_instance = TradeTransaction.from_json(json)
# print the JSON string representation of the object
print(TradeTransaction.to_json())

# convert the object into a dict
trade_transaction_dict = trade_transaction_instance.to_dict()
# create an instance of TradeTransaction from a dict
trade_transaction_from_dict = TradeTransaction.from_dict(trade_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


