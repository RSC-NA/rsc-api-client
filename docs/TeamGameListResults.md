# TeamGameListResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**goals** | **int** |  | 
**shots** | **int** |  | 
**players** | **List[str]** |  | 

## Example

```python
from rscapi.models.team_game_list_results import TeamGameListResults

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGameListResults from a JSON string
team_game_list_results_instance = TeamGameListResults.from_json(json)
# print the JSON string representation of the object
print(TeamGameListResults.to_json())

# convert the object into a dict
team_game_list_results_dict = team_game_list_results_instance.to_dict()
# create an instance of TeamGameListResults from a dict
team_game_list_results_from_dict = TeamGameListResults.from_dict(team_game_list_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


