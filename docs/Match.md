# Match


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**game_name** | **str** |  | [optional] [readonly] 
**game_pass** | **str** |  | [optional] [readonly] 
**num_games** | **int** |  | [optional] [readonly] 
**match_format** | **str** |  | [optional] [readonly] 
**match_type** | **str** |  | [optional] [readonly] 
**home_team** | [**Team**](Team.md) |  | 
**away_team** | [**Team**](Team.md) |  | 
**id** | **int** |  | [optional] [readonly] 
**results** | [**MatchResults**](MatchResults.md) |  | 

## Example

```python
from rscapi.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print(Match.to_json())

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_form_dict = match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


