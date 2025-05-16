# TrackerLinksDetailedSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] [readonly] 
**rsc_id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**discord_id** | **int** |  | [optional] [readonly] 
**platform** | **str** |  | [optional] [readonly] 
**platform_id** | **str** |  | [optional] [readonly] 
**platform_name** | **str** |  | [optional] [readonly] 
**link** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.tracker_links_detailed_sheet import TrackerLinksDetailedSheet

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinksDetailedSheet from a JSON string
tracker_links_detailed_sheet_instance = TrackerLinksDetailedSheet.from_json(json)
# print the JSON string representation of the object
print(TrackerLinksDetailedSheet.to_json())

# convert the object into a dict
tracker_links_detailed_sheet_dict = tracker_links_detailed_sheet_instance.to_dict()
# create an instance of TrackerLinksDetailedSheet from a dict
tracker_links_detailed_sheet_from_dict = TrackerLinksDetailedSheet.from_dict(tracker_links_detailed_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


