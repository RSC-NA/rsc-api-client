# ElevatedRoleLeague


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | 
**guild_id** | **int** |  | 
**active** | **bool** |  | [optional] 

## Example

```python
from rscapi.models.elevated_role_league import ElevatedRoleLeague

# TODO update the JSON string below
json = "{}"
# create an instance of ElevatedRoleLeague from a JSON string
elevated_role_league_instance = ElevatedRoleLeague.from_json(json)
# print the JSON string representation of the object
print(ElevatedRoleLeague.to_json())

# convert the object into a dict
elevated_role_league_dict = elevated_role_league_instance.to_dict()
# create an instance of ElevatedRoleLeague from a dict
elevated_role_league_from_dict = ElevatedRoleLeague.from_dict(elevated_role_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


