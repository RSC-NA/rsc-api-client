# TrackerLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | 
**discord_id** | **int** |  | 
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**platform** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**member_name** | **str** |  | [optional] [readonly] 
**platform_id** | **str** |  | [optional] [readonly] 
**rscid** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.tracker_link import TrackerLink

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLink from a JSON string
tracker_link_instance = TrackerLink.from_json(json)
# print the JSON string representation of the object
print(TrackerLink.to_json())

# convert the object into a dict
tracker_link_dict = tracker_link_instance.to_dict()
# create an instance of TrackerLink from a dict
tracker_link_form_dict = tracker_link.from_dict(tracker_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


