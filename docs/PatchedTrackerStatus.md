# PatchedTrackerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TrackerLinkStatusEnum**](TrackerLinkStatusEnum.md) |  | [optional] 

## Example

```python
from rscapi.models.patched_tracker_status import PatchedTrackerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedTrackerStatus from a JSON string
patched_tracker_status_instance = PatchedTrackerStatus.from_json(json)
# print the JSON string representation of the object
print(PatchedTrackerStatus.to_json())

# convert the object into a dict
patched_tracker_status_dict = patched_tracker_status_instance.to_dict()
# create an instance of PatchedTrackerStatus from a dict
patched_tracker_status_from_dict = PatchedTrackerStatus.from_dict(patched_tracker_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


