# CutAPlayerFromALeague

Cuts a player from their team in a given league.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to cut. | [optional] 
**league** | **int** | Guild ID of the discord the player is being cut from. | [optional] 

## Example

```python
from openapi_client.models.cut_a_player_from_a_league import CutAPlayerFromALeague

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


