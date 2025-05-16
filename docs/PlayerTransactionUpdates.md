# PlayerTransactionUpdates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**LeaguePlayer**](LeaguePlayer.md) |  | 
**old_team** | [**TransactionTeam**](TransactionTeam.md) |  | 
**new_team** | [**TransactionTeam**](TransactionTeam.md) |  | 

## Example

```python
from rscapi.models.player_transaction_updates import PlayerTransactionUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTransactionUpdates from a JSON string
player_transaction_updates_instance = PlayerTransactionUpdates.from_json(json)
# print the JSON string representation of the object
print(PlayerTransactionUpdates.to_json())

# convert the object into a dict
player_transaction_updates_dict = player_transaction_updates_instance.to_dict()
# create an instance of PlayerTransactionUpdates from a dict
player_transaction_updates_from_dict = PlayerTransactionUpdates.from_dict(player_transaction_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


