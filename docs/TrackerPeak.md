# TrackerPeak


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**rsc_id** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**discord_id** | **int** |  | [readonly] 
**status** | [**TrackerLinkStatusEnum**](TrackerLinkStatusEnum.md) |  | [readonly] 
**pulls** | **int** | Get the number of pulls for the tracker link. | [readonly] 
**peaks** | **Dict[str, int]** | Get the seasons for the tracker link. | [readonly] 

## Example

```python
from rscapi.models.tracker_peak import TrackerPeak

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerPeak from a JSON string
tracker_peak_instance = TrackerPeak.from_json(json)
# print the JSON string representation of the object
print(TrackerPeak.to_json())

# convert the object into a dict
tracker_peak_dict = tracker_peak_instance.to_dict()
# create an instance of TrackerPeak from a dict
tracker_peak_from_dict = TrackerPeak.from_dict(tracker_peak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


