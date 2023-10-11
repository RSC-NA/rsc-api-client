# SignAPlayerToATeamInALeague

Signs a player to a team in a given league..

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to sign. | [optional] 
**league** | **int** | Guild ID of the discord the player is being signed in. | [optional] 
**team** | **str** | Specific team name the player is being signed to. | [optional] 

## Example

```python
from openapi_client.models.sign_a_player_to_a_team_in_a_league import SignAPlayerToATeamInALeague

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


