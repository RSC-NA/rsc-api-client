# MatchResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**season_number** | **int** |  | [optional] [readonly] 
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**match_type** | [**MatchTypeEnum**](MatchTypeEnum.md) |  | [optional] [readonly] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | [optional] [readonly] 
**num_games** | **int** |  | [optional] [readonly] 
**tier** | **str** |  | [optional] [readonly] 
**home_team** | **str** |  | [optional] [readonly] 
**away_team** | **str** |  | [optional] [readonly] 
**home_wins** | **int** | Null until the match is reported. | [optional] [readonly] 
**away_wins** | **int** | Null until the match is reported. | [optional] [readonly] 
**home_goals** | **int** | Null until goal totals are imported. | [optional] [readonly] 
**away_goals** | **int** | Null until goal totals are imported. | [optional] [readonly] 

## Example

```python
from rscapi.models.match_result_list import MatchResultList

# TODO update the JSON string below
json = "{}"
# create an instance of MatchResultList from a JSON string
match_result_list_instance = MatchResultList.from_json(json)
# print the JSON string representation of the object
print(MatchResultList.to_json())

# convert the object into a dict
match_result_list_dict = match_result_list_instance.to_dict()
# create an instance of MatchResultList from a dict
match_result_list_from_dict = MatchResultList.from_dict(match_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


