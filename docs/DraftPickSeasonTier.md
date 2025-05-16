# DraftPickSeasonTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | [**DraftTier**](DraftTier.md) |  | 

## Example

```python
from rscapi.models.draft_pick_season_tier import DraftPickSeasonTier

# TODO update the JSON string below
json = "{}"
# create an instance of DraftPickSeasonTier from a JSON string
draft_pick_season_tier_instance = DraftPickSeasonTier.from_json(json)
# print the JSON string representation of the object
print(DraftPickSeasonTier.to_json())

# convert the object into a dict
draft_pick_season_tier_dict = draft_pick_season_tier_instance.to_dict()
# create an instance of DraftPickSeasonTier from a dict
draft_pick_season_tier_from_dict = DraftPickSeasonTier.from_dict(draft_pick_season_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


