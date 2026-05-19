# PlayerTeamInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**executor** | **int** |  | 
**admin_override** | **bool** |  | [optional] [default to False]
**notes** | **str** |  | [optional] [default to 'API Transaction']
**player** | **int** |  | 
**team** | **str** |  | 

## Example

```python
from rscapi.models.player_team_input import PlayerTeamInput

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTeamInput from a JSON string
player_team_input_instance = PlayerTeamInput.from_json(json)
# print the JSON string representation of the object
print(PlayerTeamInput.to_json())

# convert the object into a dict
player_team_input_dict = player_team_input_instance.to_dict()
# create an instance of PlayerTeamInput from a dict
player_team_input_from_dict = PlayerTeamInput.from_dict(player_team_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


