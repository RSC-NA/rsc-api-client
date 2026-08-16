# PlayerMMRExport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**discord_id** | **int** |  | 
**tier** | **str** |  | [optional] [default to '']
**current_mmr** | **int** |  | [optional] [readonly] 
**base_mmr** | **int** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.player_mmr_export import PlayerMMRExport

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerMMRExport from a JSON string
player_mmr_export_instance = PlayerMMRExport.from_json(json)
# print the JSON string representation of the object
print(PlayerMMRExport.to_json())

# convert the object into a dict
player_mmr_export_dict = player_mmr_export_instance.to_dict()
# create an instance of PlayerMMRExport from a dict
player_mmr_export_from_dict = PlayerMMRExport.from_dict(player_mmr_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


