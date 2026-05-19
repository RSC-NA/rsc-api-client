# HighLevelMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [readonly] 
**var_date** | **datetime** |  | [readonly] 
**game_name** | **str** |  | [readonly] 
**game_pass** | **str** |  | [readonly] 
**num_games** | **int** |  | [readonly] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | [readonly] 
**match_type** | [**MatchTypeEnum**](MatchTypeEnum.md) |  | [readonly] 
**home_team** | [**Team**](Team.md) |  | 
**away_team** | [**Team**](Team.md) |  | 
**id** | **int** |  | [readonly] 
**results** | [**ListMatchResults**](ListMatchResults.md) |  | 

## Example

```python
from rscapi.models.high_level_match import HighLevelMatch

# TODO update the JSON string below
json = "{}"
# create an instance of HighLevelMatch from a JSON string
high_level_match_instance = HighLevelMatch.from_json(json)
# print the JSON string representation of the object
print(HighLevelMatch.to_json())

# convert the object into a dict
high_level_match_dict = high_level_match_instance.to_dict()
# create an instance of HighLevelMatch from a dict
high_level_match_from_dict = HighLevelMatch.from_dict(high_level_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


