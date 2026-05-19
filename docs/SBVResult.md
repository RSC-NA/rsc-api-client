# SBVResult


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
**total_shots** | **int** |  | 
**pwe** | **float** |  | 
**weighted_score** | **float** |  | 
**sbv** | **float** |  | 
**metrics** | **Dict[str, float]** |  | 
**means** | **Dict[str, float]** |  | 
**stddevs** | **Dict[str, float]** |  | 
**z_scores** | **Dict[str, float]** |  | 
**correlation_weights** | **Dict[str, float]** |  | 
**settings_weights** | **Dict[str, float]** |  | 
**final_weights** | **Dict[str, float]** |  | 

## Example

```python
from rscapi.models.sbv_result import SBVResult

# TODO update the JSON string below
json = "{}"
# create an instance of SBVResult from a JSON string
sbv_result_instance = SBVResult.from_json(json)
# print the JSON string representation of the object
print(SBVResult.to_json())

# convert the object into a dict
sbv_result_dict = sbv_result_instance.to_dict()
# create an instance of SBVResult from a dict
sbv_result_from_dict = SBVResult.from_dict(sbv_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


