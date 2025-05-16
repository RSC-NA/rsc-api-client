# RetireAPlayer

Retire a player from playing in a given league

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.retire_a_player import RetireAPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of RetireAPlayer from a JSON string
retire_a_player_instance = RetireAPlayer.from_json(json)
# print the JSON string representation of the object
print(RetireAPlayer.to_json())

# convert the object into a dict
retire_a_player_dict = retire_a_player_instance.to_dict()
# create an instance of RetireAPlayer from a dict
retire_a_player_from_dict = RetireAPlayer.from_dict(retire_a_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


