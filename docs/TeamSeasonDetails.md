# TeamSeasonDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference** | [**ConferenceEnum**](ConferenceEnum.md) |  | [optional] [readonly] 
**conference_label** | **str** |  | [optional] [readonly] 
**division** | [**DivisionEnum**](DivisionEnum.md) |  | [optional] [readonly] 
**division_label** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.team_season_details import TeamSeasonDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSeasonDetails from a JSON string
team_season_details_instance = TeamSeasonDetails.from_json(json)
# print the JSON string representation of the object
print(TeamSeasonDetails.to_json())

# convert the object into a dict
team_season_details_dict = team_season_details_instance.to_dict()
# create an instance of TeamSeasonDetails from a dict
team_season_details_from_dict = TeamSeasonDetails.from_dict(team_season_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


