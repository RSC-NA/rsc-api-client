# LeaguePlayersList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[LeaguePlayer]**](LeaguePlayer.md) |  | 

## Example

```python
from rscapi.models.league_players_list200_response import LeaguePlayersList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayersList200Response from a JSON string
league_players_list200_response_instance = LeaguePlayersList200Response.from_json(json)
# print the JSON string representation of the object
print LeaguePlayersList200Response.to_json()

# convert the object into a dict
league_players_list200_response_dict = league_players_list200_response_instance.to_dict()
# create an instance of LeaguePlayersList200Response from a dict
league_players_list200_response_form_dict = league_players_list200_response.from_dict(league_players_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


