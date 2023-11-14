# LeaguePlayerMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**rsc_id** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.league_player_member import LeaguePlayerMember

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayerMember from a JSON string
league_player_member_instance = LeaguePlayerMember.from_json(json)
# print the JSON string representation of the object
print LeaguePlayerMember.to_json()

# convert the object into a dict
league_player_member_dict = league_player_member_instance.to_dict()
# create an instance of LeaguePlayerMember from a dict
league_player_member_form_dict = league_player_member.from_dict(league_player_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


