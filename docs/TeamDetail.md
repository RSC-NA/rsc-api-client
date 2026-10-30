# TeamDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**franchise** | **str** |  | [optional] 
**tier** | **str** |  | [optional] 
**players** | [**List[TeamPlayer]**](TeamPlayer.md) |  | [optional] [readonly] 
**latest_season** | **int** |  | [optional] [readonly] 
**season_details** | [**TeamSeasonDetails**](TeamSeasonDetails.md) |  | [optional] [readonly] 

## Example

```python
from rscapi.models.team_detail import TeamDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TeamDetail from a JSON string
team_detail_instance = TeamDetail.from_json(json)
# print the JSON string representation of the object
print(TeamDetail.to_json())

# convert the object into a dict
team_detail_dict = team_detail_instance.to_dict()
# create an instance of TeamDetail from a dict
team_detail_from_dict = TeamDetail.from_dict(team_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


