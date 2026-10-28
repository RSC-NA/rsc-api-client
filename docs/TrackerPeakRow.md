# TrackerPeakRow

One row of the peaks CSV: flat, unlike TrackerPeakSerializer's nested ``peaks``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**rsc_id** | **str** |  | 
**discord_id** | **int** |  | 
**name** | **str** |  | 
**pulls** | **int** |  | 
**status** | **str** |  | 
**psyonix_season** | **int** |  | 
**threes_peak_mmr** | **int** |  | 
**threes_avg_mmr** | **int** |  | 
**threes_seventy_five_mmr** | **int** |  | 
**threes_games_played** | **int** |  | 
**twos_peak_mmr** | **int** |  | 
**twos_avg_mmr** | **int** |  | 
**twos_seventy_five_mmr** | **int** |  | 
**twos_games_played** | **int** |  | 
**ones_peak_mmr** | **int** |  | 
**ones_avg_mmr** | **int** |  | 
**ones_seventy_five_mmr** | **int** |  | 
**ones_games_played** | **int** |  | 

## Example

```python
from rscapi.models.tracker_peak_row import TrackerPeakRow

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerPeakRow from a JSON string
tracker_peak_row_instance = TrackerPeakRow.from_json(json)
# print the JSON string representation of the object
print(TrackerPeakRow.to_json())

# convert the object into a dict
tracker_peak_row_dict = tracker_peak_row_instance.to_dict()
# create an instance of TrackerPeakRow from a dict
tracker_peak_row_from_dict = TrackerPeakRow.from_dict(tracker_peak_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


