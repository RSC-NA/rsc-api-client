# FlaggedMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**day** | **int** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] [readonly] 
**match_type** | [**MatchTypeEnum**](MatchTypeEnum.md) |  | 
**match_type_label** | **str** |  | 
**tier** | **str** |  | 
**home_team** | **str** |  | 
**away_team** | **str** |  | 
**home_gm_discord_id** | **int** |  | 
**away_gm_discord_id** | **int** |  | 
**home_wins** | **int** |  | 
**away_wins** | **int** |  | 
**ballchasing_group** | **str** |  | 
**reported_games** | **int** |  | [optional] [readonly] 
**expected_games** | **int** |  | [optional] [readonly] 
**missing_result** | **bool** |  | [optional] [readonly] 
**missing_ballchasing_group** | **bool** |  | [optional] [readonly] 
**missing_stats** | **bool** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.flagged_match import FlaggedMatch

# TODO update the JSON string below
json = "{}"
# create an instance of FlaggedMatch from a JSON string
flagged_match_instance = FlaggedMatch.from_json(json)
# print the JSON string representation of the object
print(FlaggedMatch.to_json())

# convert the object into a dict
flagged_match_dict = flagged_match_instance.to_dict()
# create an instance of FlaggedMatch from a dict
flagged_match_from_dict = FlaggedMatch.from_dict(flagged_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


