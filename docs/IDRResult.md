# IDRResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | [optional] 
**league_player_id** | **int** |  | 
**discord_id** | **int** |  | 
**player_name** | **str** |  | 
**tier_id** | **int** |  | 
**tier_name** | **str** |  | 
**games_played** | **int** |  | 
**win_percentage** | **float** |  | 
**pwe** | **float** |  | 
**performance_index** | **float** | Weighted sum of the indexes, before standardizing against the tier. | 
**idr** | **float** |  | 
**outlier_value** | **float** | Roughly how many more players you would have to see before seeing one this far from average. | 
**is_qualified** | **bool** | Whether the player met the tier&#39;s games-played threshold. | 
**qualification_threshold** | **int** | Games played required to be a qualified player in this tier. | 
**computed_at** | **datetime** | When the stored IDR was last recomputed. Null if computed on the fly. | [optional] 
**per_game** | **Dict[str, float]** |  | 
**against_per_game** | **Dict[str, float]** |  | 
**opponent_per_game** | **Dict[str, float]** |  | 
**opponent_against_per_game** | **Dict[str, float]** |  | 
**metrics** | **Dict[str, float]** |  | 
**stat_means** | **Dict[str, float]** |  | 
**metric_means** | **Dict[str, float]** |  | 
**metric_stddevs** | **Dict[str, float]** |  | 
**correlations_win** | **Dict[str, float]** |  | 
**correlations_pwe** | **Dict[str, float]** |  | 
**settings_weights** | **Dict[str, float]** |  | 
**final_weights** | **Dict[str, float]** |  | 

## Example

```python
from rscapi.models.idr_result import IDRResult

# TODO update the JSON string below
json = "{}"
# create an instance of IDRResult from a JSON string
idr_result_instance = IDRResult.from_json(json)
# print the JSON string representation of the object
print(IDRResult.to_json())

# convert the object into a dict
idr_result_dict = idr_result_instance.to_dict()
# create an instance of IDRResult from a dict
idr_result_from_dict = IDRResult.from_dict(idr_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


