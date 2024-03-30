# TrackerLinkInvalidateObject

Request body object containing a dictionary 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **List[str]** | List of links to invalidate | 

## Example

```python
from rscapi.models.tracker_link_invalidate_object import TrackerLinkInvalidateObject

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinkInvalidateObject from a JSON string
tracker_link_invalidate_object_instance = TrackerLinkInvalidateObject.from_json(json)
# print the JSON string representation of the object
print(TrackerLinkInvalidateObject.to_json())

# convert the object into a dict
tracker_link_invalidate_object_dict = tracker_link_invalidate_object_instance.to_dict()
# create an instance of TrackerLinkInvalidateObject from a dict
tracker_link_invalidate_object_form_dict = tracker_link_invalidate_object.from_dict(tracker_link_invalidate_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


