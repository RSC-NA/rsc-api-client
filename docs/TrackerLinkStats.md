# TrackerLinkStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from rscapi.models.tracker_link_stats import TrackerLinkStats

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinkStats from a JSON string
tracker_link_stats_instance = TrackerLinkStats.from_json(json)
# print the JSON string representation of the object
print(TrackerLinkStats.to_json())

# convert the object into a dict
tracker_link_stats_dict = tracker_link_stats_instance.to_dict()
# create an instance of TrackerLinkStats from a dict
tracker_link_stats_from_dict = TrackerLinkStats.from_dict(tracker_link_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


