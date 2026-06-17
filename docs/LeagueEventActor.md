# LeagueEventActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.league_event_actor import LeagueEventActor

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueEventActor from a JSON string
league_event_actor_instance = LeagueEventActor.from_json(json)
# print the JSON string representation of the object
print(LeagueEventActor.to_json())

# convert the object into a dict
league_event_actor_dict = league_event_actor_instance.to_dict()
# create an instance of LeagueEventActor from a dict
league_event_actor_from_dict = LeagueEventActor.from_dict(league_event_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


