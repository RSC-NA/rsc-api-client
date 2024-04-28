# DraftAPlayerToATeam

Draft a player to a specific team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | **int** | Specific player to perform transaction on. | [optional] 
**league** | **int** | ID of the league transaction is for. | [optional] 
**team** | **str** | Specific team name for the transaction. | [optional] 
**executor** | **int** | Discord ID of specific member who ran the transaction. | [optional] 
**admin_override** | **bool** | Boolean indicating whether or not an admin is overriding this command. | [optional] 
**round** | **int** | Specific round player was drafted in. | [optional] 
**number** | **int** | Specific number was drafted at. | [optional] 

## Example

```python
from rscapi.models.draft_a_player_to_a_team import DraftAPlayerToATeam

# TODO update the JSON string below
json = "{}"
# create an instance of DraftAPlayerToATeam from a JSON string
draft_a_player_to_a_team_instance = DraftAPlayerToATeam.from_json(json)
# print the JSON string representation of the object
print(DraftAPlayerToATeam.to_json())

# convert the object into a dict
draft_a_player_to_a_team_dict = draft_a_player_to_a_team_instance.to_dict()
# create an instance of DraftAPlayerToATeam from a dict
draft_a_player_to_a_team_form_dict = draft_a_player_to_a_team.from_dict(draft_a_player_to_a_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


