# TradeValue

The specific item being traded (player or pick)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**Player1**](Player1.md) |  | [optional] 
**pick** | [**DraftPick**](DraftPick.md) |  | [optional] 

## Example

```python
from rscapi.models.trade_value import TradeValue

# TODO update the JSON string below
json = "{}"
# create an instance of TradeValue from a JSON string
trade_value_instance = TradeValue.from_json(json)
# print the JSON string representation of the object
print(TradeValue.to_json())

# convert the object into a dict
trade_value_dict = trade_value_instance.to_dict()
# create an instance of TradeValue from a dict
trade_value_from_dict = TradeValue.from_dict(trade_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


