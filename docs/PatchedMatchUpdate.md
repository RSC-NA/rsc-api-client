# PatchedMatchUpdate

PUT/PATCH on a match: its schedule and lobby, never its teams or season.  The generic update used MatchListSerializer, whose dotted-source team fields made every PUT a 500 and silently ignored most PATCHes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**num_games** | **int** |  | [optional] 
**game_name** | **str** |  | [optional] 
**game_pass** | **str** |  | [optional] 
**match_format** | [**MatchFormatEnum**](MatchFormatEnum.md) |  | [optional] 
**match_type** | [**PlayableMatchTypeEnum**](PlayableMatchTypeEnum.md) |  | [optional] 
**streamed_match** | **bool** |  | [optional] 

## Example

```python
from rscapi.models.patched_match_update import PatchedMatchUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMatchUpdate from a JSON string
patched_match_update_instance = PatchedMatchUpdate.from_json(json)
# print the JSON string representation of the object
print(PatchedMatchUpdate.to_json())

# convert the object into a dict
patched_match_update_dict = patched_match_update_instance.to_dict()
# create an instance of PatchedMatchUpdate from a dict
patched_match_update_from_dict = PatchedMatchUpdate.from_dict(patched_match_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


