# TradeObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**TradeFranchise**](TradeFranchise.md) |  | 
**destination** | [**TradeFranchise**](TradeFranchise.md) |  | 
**value** | [**TradeItem**](TradeItem.md) |  | 

## Example

```python
from rscapi.models.trade_object import TradeObject

# TODO update the JSON string below
json = "{}"
# create an instance of TradeObject from a JSON string
trade_object_instance = TradeObject.from_json(json)
# print the JSON string representation of the object
print(TradeObject.to_json())

# convert the object into a dict
trade_object_dict = trade_object_instance.to_dict()
# create an instance of TradeObject from a dict
trade_object_from_dict = TradeObject.from_dict(trade_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


