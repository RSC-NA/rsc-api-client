# PlayerTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**franchise** | [**PlayerFranchise**](PlayerFranchise.md) |  | [optional] 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.player_team import PlayerTeam

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerTeam from a JSON string
player_team_instance = PlayerTeam.from_json(json)
# print the JSON string representation of the object
print(PlayerTeam.to_json())

# convert the object into a dict
player_team_dict = player_team_instance.to_dict()
# create an instance of PlayerTeam from a dict
player_team_from_dict = PlayerTeam.from_dict(player_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


