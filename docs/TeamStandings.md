# TeamStandings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**franchise** | **str** |  | 
**team** | **str** |  | 
**tier** | **str** |  | 
**rank** | **int** |  | 
**games_played** | **int** |  | [optional] [readonly] 
**games_won** | **int** |  | [optional] [readonly] 
**games_lost** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.team_standings import TeamStandings

# TODO update the JSON string below
json = "{}"
# create an instance of TeamStandings from a JSON string
team_standings_instance = TeamStandings.from_json(json)
# print the JSON string representation of the object
print(TeamStandings.to_json())

# convert the object into a dict
team_standings_dict = team_standings_instance.to_dict()
# create an instance of TeamStandings from a dict
team_standings_from_dict = TeamStandings.from_dict(team_standings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


