# MatchList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**game_name** | **str** |  | [optional] [readonly] 
**game_pass** | **str** |  | [optional] [readonly] 
**num_games** | **int** |  | [optional] [readonly] 
**match_format** | **str** |  | 
**match_type** | **str** |  | 
**home_team** | **str** |  | 
**away_team** | **str** |  | 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.match_list import MatchList

# TODO update the JSON string below
json = "{}"
# create an instance of MatchList from a JSON string
match_list_instance = MatchList.from_json(json)
# print the JSON string representation of the object
print MatchList.to_json()

# convert the object into a dict
match_list_dict = match_list_instance.to_dict()
# create an instance of MatchList from a dict
match_list_form_dict = match_list.from_dict(match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


