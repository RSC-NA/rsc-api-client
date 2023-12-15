# PlayerTrade

Trade two players between franchises

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_player** | **int** | Specific player to perform transaction on. | [optional] 
**second_player** | **int** | Specific player to perform transaction on. | [optional] 
**league** | **int** | ID of the league transaction is for. | 
**team** | **str** | Specific team name for the transaction. | [optional] 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.player_trade import PlayerTrade

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTrade from a JSON string
player_trade_instance = PlayerTrade.from_json(json)
# print the JSON string representation of the object
print PlayerTrade.to_json()

# convert the object into a dict
player_trade_dict = player_trade_instance.to_dict()
# create an instance of PlayerTrade from a dict
player_trade_form_dict = player_trade.from_dict(player_trade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


