# TrackerLinksSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsc_id** | **str** |  | 
**name** | **str** |  | 
**link** | **str** |  | [optional] [readonly] 

## Example

```python
from rscapi.models.tracker_links_sheet import TrackerLinksSheet

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinksSheet from a JSON string
tracker_links_sheet_instance = TrackerLinksSheet.from_json(json)
# print the JSON string representation of the object
print(TrackerLinksSheet.to_json())

# convert the object into a dict
tracker_links_sheet_dict = tracker_links_sheet_instance.to_dict()
# create an instance of TrackerLinksSheet from a dict
tracker_links_sheet_from_dict = TrackerLinksSheet.from_dict(tracker_links_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


