# SignAPlayerToATeamInALeague

Signs a player to a team in a given league..

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | 
**league** | **int** | ID of the league transaction is for. | 
**team** | **str** | Specific team name for the transaction. | 
**executor** | **int** | Discord ID of specific member who ran the transaction. | 
**admin_override** | **int** | Boolean indicating whether or not an admin is overriding this command. | [optional] 

## Example

```python
from rscapi.models.sign_a_player_to_a_team_in_a_league import SignAPlayerToATeamInALeague

# TODO update the JSON string below
json = "{}"
# create an instance of SignAPlayerToATeamInALeague from a JSON string
sign_a_player_to_a_team_in_a_league_instance = SignAPlayerToATeamInALeague.from_json(json)
# print the JSON string representation of the object
print SignAPlayerToATeamInALeague.to_json()

# convert the object into a dict
sign_a_player_to_a_team_in_a_league_dict = sign_a_player_to_a_team_in_a_league_instance.to_dict()
# create an instance of SignAPlayerToATeamInALeague from a dict
sign_a_player_to_a_team_in_a_league_form_dict = sign_a_player_to_a_team_in_a_league.from_dict(sign_a_player_to_a_team_in_a_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


