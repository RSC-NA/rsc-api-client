# PaginatedLeaguePlayerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LeaguePlayer]**](LeaguePlayer.md) |  | 

## Example

```python
from rscapi.models.paginated_league_player_list import PaginatedLeaguePlayerList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLeaguePlayerList from a JSON string
paginated_league_player_list_instance = PaginatedLeaguePlayerList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLeaguePlayerList.to_json())

# convert the object into a dict
paginated_league_player_list_dict = paginated_league_player_list_instance.to_dict()
# create an instance of PaginatedLeaguePlayerList from a dict
paginated_league_player_list_from_dict = PaginatedLeaguePlayerList.from_dict(paginated_league_player_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


