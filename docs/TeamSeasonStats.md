# TeamSeasonStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**team** | **str** |  | 
**type** | **str** |  | 
**shooting_percentage** | **float** |  | 
**win_percentage** | **float** |  | 
**goal_differential** | **int** |  | 
**opponent_shooting_percentage** | **float** |  | 
**stats_type** | **str** |  | [optional] 
**games_played** | **int** |  | [optional] 
**games_won** | **int** |  | [optional] 
**games_lost** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**goals** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**saves** | **int** |  | [optional] 
**shots** | **int** |  | [optional] 
**opponent_points** | **int** |  | [optional] 
**opponent_goals** | **int** |  | [optional] 
**opponent_assists** | **int** |  | [optional] 
**opponent_saves** | **int** |  | [optional] 
**opponent_shots** | **int** |  | [optional] 
**demos_inflicted** | **int** |  | [optional] 
**demos_taken** | **int** |  | [optional] 

## Example

```python
from rscapi.models.team_season_stats import TeamSeasonStats

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonStats from a JSON string
team_season_stats_instance = TeamSeasonStats.from_json(json)
# print the JSON string representation of the object
print(TeamSeasonStats.to_json())

# convert the object into a dict
team_season_stats_dict = team_season_stats_instance.to_dict()
# create an instance of TeamSeasonStats from a dict
team_season_stats_form_dict = team_season_stats.from_dict(team_season_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


