# DraftTierCountKeeperExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_player_id** | **int** |  | 
**rsc_id** | **str** |  | 
**player_name** | **str** |  | 
**discord_id** | **int** |  | 
**base_mmr** | **int** |  | 
**effective_mmr** | **int** |  | 
**tier_data** | **str** |  | 
**count** | **int** |  | 
**keeper** | **int** |  | 

## Example

```python
from rscapi.models.draft_tier_count_keeper_export import DraftTierCountKeeperExport

# TODO update the JSON string below
json = "{}"
# create an instance of DraftTierCountKeeperExport from a JSON string
draft_tier_count_keeper_export_instance = DraftTierCountKeeperExport.from_json(json)
# print the JSON string representation of the object
print(DraftTierCountKeeperExport.to_json())

# convert the object into a dict
draft_tier_count_keeper_export_dict = draft_tier_count_keeper_export_instance.to_dict()
# create an instance of DraftTierCountKeeperExport from a dict
draft_tier_count_keeper_export_from_dict = DraftTierCountKeeperExport.from_dict(draft_tier_count_keeper_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


