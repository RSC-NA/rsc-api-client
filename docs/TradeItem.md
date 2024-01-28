# TradeItem

An item in a trade detailing what's being traded.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**FranchiseIdentifier**](FranchiseIdentifier.md) |  | 
**destination** | [**FranchiseIdentifier**](FranchiseIdentifier.md) |  | 
**value** | [**TradeValue**](TradeValue.md) |  | 

## Example

```python
from rscapi.models.trade_item import TradeItem

# TODO update the JSON string below
json = "{}"
# create an instance of TradeItem from a JSON string
trade_item_instance = TradeItem.from_json(json)
# print the JSON string representation of the object
print TradeItem.to_json()

# convert the object into a dict
trade_item_dict = trade_item_instance.to_dict()
# create an instance of TradeItem from a dict
trade_item_form_dict = trade_item.from_dict(trade_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


