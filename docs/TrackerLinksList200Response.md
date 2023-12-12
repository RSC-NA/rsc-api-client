# TrackerLinksList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TrackerLink]**](TrackerLink.md) |  | 

## Example

```python
from rscapi.models.tracker_links_list200_response import TrackerLinksList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerLinksList200Response from a JSON string
tracker_links_list200_response_instance = TrackerLinksList200Response.from_json(json)
# print the JSON string representation of the object
print TrackerLinksList200Response.to_json()

# convert the object into a dict
tracker_links_list200_response_dict = tracker_links_list200_response_instance.to_dict()
# create an instance of TrackerLinksList200Response from a dict
tracker_links_list200_response_form_dict = tracker_links_list200_response.from_dict(tracker_links_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


