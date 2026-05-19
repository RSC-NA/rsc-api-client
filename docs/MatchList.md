# MatchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [readonly] 
**var_date** | **datetime** |  | [readonly] 
**game_name** | **str** |  | [readonly] 
**game_pass** | **str** |  | [readonly] 
**num_games** | **int** |  | [readonly] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | 
**match_type** | [**MatchTypeEnum**](MatchTypeEnum.md) |  | 
**home_team** | **str** |  | 
**away_team** | **str** |  | 
**id** | **int** |  | [readonly] 

## Example

```python
from rscapi.models.match_list import MatchList

# TODO update the JSON string below
json = "{}"
# create an instance of MatchList from a JSON string
match_list_instance = MatchList.from_json(json)
# print the JSON string representation of the object
print(MatchList.to_json())

# convert the object into a dict
match_list_dict = match_list_instance.to_dict()
# create an instance of MatchList from a dict
match_list_from_dict = MatchList.from_dict(match_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


