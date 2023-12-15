# TeamGameListResultsField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**goals** | **int** |  | 
**shots** | **int** |  | 
**players** | **List[str]** |  | 

## Example

```python
from rscapi.models.team_game_list_results_field import TeamGameListResultsField

# TODO update the JSON string below
json = "{}"
# create an instance of TeamGameListResultsField from a JSON string
team_game_list_results_field_instance = TeamGameListResultsField.from_json(json)
# print the JSON string representation of the object
print TeamGameListResultsField.to_json()

# convert the object into a dict
team_game_list_results_field_dict = team_game_list_results_field_instance.to_dict()
# create an instance of TeamGameListResultsField from a dict
team_game_list_results_field_form_dict = team_game_list_results_field.from_dict(team_game_list_results_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


