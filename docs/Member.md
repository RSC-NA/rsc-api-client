# Member


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**rsc_id** | **str** |  | [optional] [readonly] 
**elevated_roles** | [**List[ElevatedRole]**](ElevatedRole.md) |  | [optional] [readonly] 
**player_leagues** | [**List[LeaguePlayer]**](LeaguePlayer.md) |  | [optional] [readonly] 
**rsc_name** | **str** |  | [optional] 
**discord_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print Member.to_json()

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_form_dict = member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


