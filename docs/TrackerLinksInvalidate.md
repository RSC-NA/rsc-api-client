# TrackerLinksInvalidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[str]** | Tracker link URLs to mark failed. | 

## Example

```python
from rscapi.models.tracker_links_invalidate import TrackerLinksInvalidate

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinksInvalidate from a JSON string
tracker_links_invalidate_instance = TrackerLinksInvalidate.from_json(json)
# print the JSON string representation of the object
print(TrackerLinksInvalidate.to_json())

# convert the object into a dict
tracker_links_invalidate_dict = tracker_links_invalidate_instance.to_dict()
# create an instance of TrackerLinksInvalidate from a dict
tracker_links_invalidate_from_dict = TrackerLinksInvalidate.from_dict(tracker_links_invalidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


