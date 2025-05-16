# SeasonLeague


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.season_league import SeasonLeague

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonLeague from a JSON string
season_league_instance = SeasonLeague.from_json(json)
# print the JSON string representation of the object
print(SeasonLeague.to_json())

# convert the object into a dict
season_league_dict = season_league_instance.to_dict()
# create an instance of SeasonLeague from a dict
season_league_from_dict = SeasonLeague.from_dict(season_league_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


