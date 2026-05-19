# PatchedLeague


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**guild_id** | **int** |  | [optional] 
**active** | **bool** |  | [optional] 
**league_data** | [**LeagueData**](LeagueData.md) |  | [optional] 
**tiers** | [**List[Tier]**](Tier.md) |  | [optional] 

## Example

```python
from rscapi.models.patched_league import PatchedLeague

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLeague from a JSON string
patched_league_instance = PatchedLeague.from_json(json)
# print the JSON string representation of the object
print(PatchedLeague.to_json())

# convert the object into a dict
patched_league_dict = patched_league_instance.to_dict()
# create an instance of PatchedLeague from a dict
patched_league_from_dict = PatchedLeague.from_dict(patched_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


