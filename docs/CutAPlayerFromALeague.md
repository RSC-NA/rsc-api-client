# CutAPlayerFromALeague

Cuts a player from their team in a given league.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.cut_a_player_from_a_league import CutAPlayerFromALeague

# TODO update the JSON string below
json = "{}"
# create an instance of CutAPlayerFromALeague from a JSON string
cut_a_player_from_a_league_instance = CutAPlayerFromALeague.from_json(json)
# print the JSON string representation of the object
print CutAPlayerFromALeague.to_json()

# convert the object into a dict
cut_a_player_from_a_league_dict = cut_a_player_from_a_league_instance.to_dict()
# create an instance of CutAPlayerFromALeague from a dict
cut_a_player_from_a_league_form_dict = cut_a_player_from_a_league.from_dict(cut_a_player_from_a_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


