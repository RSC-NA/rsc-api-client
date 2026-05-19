# TradePlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**team** | **str** |  | 

## Example

```python
from rscapi.models.trade_player import TradePlayer

# TODO update the JSON string below
json = "{}"
# create an instance of TradePlayer from a JSON string
trade_player_instance = TradePlayer.from_json(json)
# print the JSON string representation of the object
print(TradePlayer.to_json())

# convert the object into a dict
trade_player_dict = trade_player_instance.to_dict()
# create an instance of TradePlayer from a dict
trade_player_from_dict = TradePlayer.from_dict(trade_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


