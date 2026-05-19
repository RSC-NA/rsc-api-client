# PatchedMatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**game_name** | **str** |  | [optional] [readonly] 
**game_pass** | **str** |  | [optional] [readonly] 
**num_games** | **int** |  | [optional] [readonly] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | [optional] 
**match_type** | [**MatchTypeEnum**](MatchTypeEnum.md) |  | [optional] 
**home_team** | **str** |  | [optional] 
**away_team** | **str** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.patched_match_list import PatchedMatchList

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMatchList from a JSON string
patched_match_list_instance = PatchedMatchList.from_json(json)
# print the JSON string representation of the object
print(PatchedMatchList.to_json())

# convert the object into a dict
patched_match_list_dict = patched_match_list_instance.to_dict()
# create an instance of PatchedMatchList from a dict
patched_match_list_from_dict = PatchedMatchList.from_dict(patched_match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


