# LeagueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_num_players** | **int** |  | [optional] 
**game_mode** | **str** |  | [optional] 
**match_format** | **int** |  | [optional] 

## Example

```python
from rscapi.models.league_data import LeagueData

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueData from a JSON string
league_data_instance = LeagueData.from_json(json)
# print the JSON string representation of the object
print(LeagueData.to_json())

# convert the object into a dict
league_data_dict = league_data_instance.to_dict()
# create an instance of LeagueData from a dict
league_data_from_dict = LeagueData.from_dict(league_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


