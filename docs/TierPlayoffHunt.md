# TierPlayoffHunt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier_id** | **int** |  | 
**tier_name** | **str** |  | 
**tier_position** | **int** |  | 
**playoff_format** | [**PlayoffFormatEnum**](PlayoffFormatEnum.md) |  | 
**playoff_format_label** | **str** |  | 
**playoff_format_source** | [**PlayoffFormatSourceEnum**](PlayoffFormatSourceEnum.md) | Inferred when the season has no format set for the tier.  * &#x60;configured&#x60; - configured * &#x60;inferred&#x60; - inferred | 
**regular_season_complete** | **bool** |  | 
**groups** | [**List[PlayoffGroup]**](PlayoffGroup.md) |  | 

## Example

```python
from rscapi.models.tier_playoff_hunt import TierPlayoffHunt

# TODO update the JSON string below
json = "{}"
# create an instance of TierPlayoffHunt from a JSON string
tier_playoff_hunt_instance = TierPlayoffHunt.from_json(json)
# print the JSON string representation of the object
print(TierPlayoffHunt.to_json())

# convert the object into a dict
tier_playoff_hunt_dict = tier_playoff_hunt_instance.to_dict()
# create an instance of TierPlayoffHunt from a dict
tier_playoff_hunt_from_dict = TierPlayoffHunt.from_dict(tier_playoff_hunt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


