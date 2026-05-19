# PatchedMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**rsc_id** | **str** |  | [optional] [readonly] 
**elevated_roles** | [**List[ElevatedRole]**](ElevatedRole.md) |  | [optional] [readonly] 
**player_leagues** | [**List[LeaguePlayer]**](LeaguePlayer.md) |  | [optional] [readonly] 
**rsc_name** | **str** |  | [optional] 
**discord_id** | **int** |  | [optional] 

## Example

```python
from rscapi.models.patched_member import PatchedMember

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMember from a JSON string
patched_member_instance = PatchedMember.from_json(json)
# print the JSON string representation of the object
print(PatchedMember.to_json())

# convert the object into a dict
patched_member_dict = patched_member_instance.to_dict()
# create an instance of PatchedMember from a dict
patched_member_from_dict = PatchedMember.from_dict(patched_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


