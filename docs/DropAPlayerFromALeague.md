# DropAPlayerFromALeague

Drops a player from a league (prior to regular season)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** | League of team player will be dropped from | 

## Example

```python
from rscapi.models.drop_a_player_from_a_league import DropAPlayerFromALeague

# TODO update the JSON string below
json = "{}"
# create an instance of DropAPlayerFromALeague from a JSON string
drop_a_player_from_a_league_instance = DropAPlayerFromALeague.from_json(json)
# print the JSON string representation of the object
print(DropAPlayerFromALeague.to_json())

# convert the object into a dict
drop_a_player_from_a_league_dict = drop_a_player_from_a_league_instance.to_dict()
# create an instance of DropAPlayerFromALeague from a dict
drop_a_player_from_a_league_from_dict = DropAPlayerFromALeague.from_dict(drop_a_player_from_a_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


