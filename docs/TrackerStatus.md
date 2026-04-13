# TrackerStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from rscapi.models.tracker_status import TrackerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerStatus from a JSON string
tracker_status_instance = TrackerStatus.from_json(json)
# print the JSON string representation of the object
print(TrackerStatus.to_json())

# convert the object into a dict
tracker_status_dict = tracker_status_instance.to_dict()
# create an instance of TrackerStatus from a dict
tracker_status_from_dict = TrackerStatus.from_dict(tracker_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


