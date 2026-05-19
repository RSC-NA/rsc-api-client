# LeagueSeasonStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**preseason_start_date** | **str** |  | 
**regular_season_start** | **str** |  | 
**regular_season_end** | **str** |  | 
**draft_date** | **str** |  | 
**signups_close** | **str** |  | 
**season_number** | **int** |  | [optional] 

## Example

```python
from rscapi.models.league_season_start import LeagueSeasonStart

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueSeasonStart from a JSON string
league_season_start_instance = LeagueSeasonStart.from_json(json)
# print the JSON string representation of the object
print(LeagueSeasonStart.to_json())

# convert the object into a dict
league_season_start_dict = league_season_start_instance.to_dict()
# create an instance of LeagueSeasonStart from a dict
league_season_start_from_dict = LeagueSeasonStart.from_dict(league_season_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


