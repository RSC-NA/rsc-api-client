# LeaguePlayerSignup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league** | **int** |  | 
**team_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**base_mmr** | **int** |  | 
**current_mmr** | **int** |  | 
**tier** | **int** |  | 
**contract_length** | **int** |  | [optional] 

## Example

```python
from rscapi.models.league_player_signup import LeaguePlayerSignup

# TODO update the JSON string below
json = "{}"
# create an instance of LeaguePlayerSignup from a JSON string
league_player_signup_instance = LeaguePlayerSignup.from_json(json)
# print the JSON string representation of the object
print(LeaguePlayerSignup.to_json())

# convert the object into a dict
league_player_signup_dict = league_player_signup_instance.to_dict()
# create an instance of LeaguePlayerSignup from a dict
league_player_signup_from_dict = LeaguePlayerSignup.from_dict(league_player_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


