# ReSignPlayer

Re-sign a player to a franchise.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | 
**team** | **str** | Specific team name for the transaction. | 
**league** | **int** | ID of the league transaction is for. | 
**notes** | **str** | Notes for the transaction from the TM running it. | [optional] 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.re_sign_player import ReSignPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of ReSignPlayer from a JSON string
re_sign_player_instance = ReSignPlayer.from_json(json)
# print the JSON string representation of the object
print(ReSignPlayer.to_json())

# convert the object into a dict
re_sign_player_dict = re_sign_player_instance.to_dict()
# create an instance of ReSignPlayer from a dict
re_sign_player_form_dict = re_sign_player.from_dict(re_sign_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


