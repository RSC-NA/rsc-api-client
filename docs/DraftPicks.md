# DraftPicks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Pick in the specific tier. | [optional] 
**round** | **int** | Specific round in the tier. | [optional] 
**gm** | **int** |  | 
**season_tier** | [**DraftPickSeasonTier**](DraftPickSeasonTier.md) |  | 

## Example

```python
from rscapi.models.draft_picks import DraftPicks

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPicks from a JSON string
draft_picks_instance = DraftPicks.from_json(json)
# print the JSON string representation of the object
print(DraftPicks.to_json())

# convert the object into a dict
draft_picks_dict = draft_picks_instance.to_dict()
# create an instance of DraftPicks from a dict
draft_picks_from_dict = DraftPicks.from_dict(draft_picks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


