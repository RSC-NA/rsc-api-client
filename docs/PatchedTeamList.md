# PatchedTeamList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**franchise** | [**TeamFranchise**](TeamFranchise.md) |  | [optional] 
**tier** | [**Tier**](Tier.md) |  | [optional] 

## Example

```python
from rscapi.models.patched_team_list import PatchedTeamList

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTeamList from a JSON string
patched_team_list_instance = PatchedTeamList.from_json(json)
# print the JSON string representation of the object
print(PatchedTeamList.to_json())

# convert the object into a dict
patched_team_list_dict = patched_team_list_instance.to_dict()
# create an instance of PatchedTeamList from a dict
patched_team_list_from_dict = PatchedTeamList.from_dict(patched_team_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


