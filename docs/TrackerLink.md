# TrackerLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** |  | 
**member** | [**Really**](Really.md) |  | [readonly] 
**discord_id** | **int** |  | [optional] 
**id** | **int** |  | [readonly] 
**name** | **str** |  | [readonly] 
**pulls** | **int** |  | [readonly] 
**platform** | [**PlatformEnum**](PlatformEnum.md) |  | [readonly] 
**status** | [**TrackerLinkStatusEnum**](TrackerLinkStatusEnum.md) |  | [readonly] 
**last_updated** | **datetime** |  | [readonly] 
**member_name** | **str** |  | [readonly] 
**platform_id** | **str** |  | [readonly] 
**rscid** | **str** |  | [readonly] 

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
tracker_link_from_dict = TrackerLink.from_dict(tracker_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


