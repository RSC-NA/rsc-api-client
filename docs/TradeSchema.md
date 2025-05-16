# TradeSchema

Schema for Pick/Player trades

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trades** | [**List[TradeItem]**](TradeItem.md) | List of trades to execute | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 

## Example

```python
from rscapi.models.trade_schema import TradeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TradeSchema from a JSON string
trade_schema_instance = TradeSchema.from_json(json)
# print the JSON string representation of the object
print(TradeSchema.to_json())

# convert the object into a dict
trade_schema_dict = trade_schema_instance.to_dict()
# create an instance of TradeSchema from a dict
trade_schema_from_dict = TradeSchema.from_dict(trade_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


